import motor_driver
import encoder_reader
import motor_controller
import utime
import pyb

"""!
    @file                       main.py
    @brief                      Test
    @details                    This is .
                                
    @author                     Peyton Archibald
    @author                     Harrison Hirsch
    @date                       January 31, 2023
"""


def main():
    # periodic_step_test()
    step_response_test()

    # for number in range(10):  # Just some example output
    #     u2.write(f"Count: {number}\r\n")  # The "\r\n" is end-of-line stuff
    #     number += 1


def periodic_step_test():
    motor1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3)  # Set up motor 1
    encoder1 = encoder_reader.EncoderReader('C6', 'C7', 8)  # Set up encoder 1
    setpt = 16348
    controller1 = motor_controller.MotorController(.01, setpt)  # Set up controller 1
    startTime = utime.ticks_ms()
    currTime = 0
    while True:
        try:
            if currTime >= 3000:
                startTime = utime.ticks_ms()
                setpt += 16348
                controller1.set_setpoint(setpt)
            encoderPosSpeed = encoder1.read()
            desiredDuty = controller1.run(encoderPosSpeed[0])
            motor1.set_duty_cycle(desiredDuty)
            utime.sleep_ms(10)
            stopTime = utime.ticks_ms()
            currTime = utime.ticks_diff(stopTime, startTime)
            # print(currTime)
        except KeyboardInterrupt:
            break
    motor1.set_duty_cycle(0)


def step_response_test():
    while True:
        motor1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3)  # Set up motor 1
        encoder1 = encoder_reader.EncoderReader('C6', 'C7', 8)  # Set up encoder 1
        setpt = 16348
        Kp_input = input('Enter a Kp: ')
        if is_number(Kp_input):
            Kp_input = float(Kp_input)
        else:
            raise ValueError('Input must be a number')
        controller1 = motor_controller.MotorController(Kp_input, setpt)  # Set up controller 1
        u2 = pyb.UART(2, baudrate=115200)  # Set up the second USB-serial port
        startTime = utime.ticks_ms()
        currTime = 0
        initial_val_lst = 100 * [0]
        final_value_lst = 500 * [24000]
        step_lst = initial_val_lst + final_value_lst
        storedData = []
        for value in step_lst:
            encoderPosSpeed = encoder1.read()
            controller1.set_setpoint(value)
            desiredDuty = controller1.run(encoderPosSpeed[0])
            motor1.set_duty_cycle(desiredDuty)
            stopTime = utime.ticks_ms()
            currTime = utime.ticks_diff(stopTime, startTime)
            currPos = encoderPosSpeed[0]
            controller1.store_data(storedData, currTime, currPos)
            utime.sleep_ms(10)
        for dataPt in storedData:
            u2.write(f'{dataPt[0]}, {dataPt[1]}\r\n')


def is_number(pt):          # Helper function to test if number
    try:
        float(pt)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
