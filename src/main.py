import motor_driver
import encoder_reader
import motor_controller
import utime

"""!
    @file                       main.py
    @brief                      Test
    @details                    This is .
                                
    @author                     Peyton Archibald
    @author                     Harrison Hirsch
    @date                       January 31, 2023
"""


def main():
    periodic_step_test()


def periodic_step_test():
    motor1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3)  # Set up motor 1
    encoder1 = encoder_reader.EncoderReader('C6', 'C7', 8)  # Set up encoder 1
    setpt = 16348
    controller1 = motor_controller.MotorController(.1, setpt)  # Set up controller 1
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
            print(currTime)
        except KeyboardInterrupt:
            break
    motor1.set_duty_cycle(0)


def step_response_test():
    motor1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3)  # Set up motor 1
    encoder1 = encoder_reader.EncoderReader('C6', 'C7', 8)  # Set up encoder 1
    setpt = 16348
    controller1 = motor_controller.MotorController(.1, setpt)  # Set up controller 1
    startTime = utime.ticks_ms()
    initial_val_lst = 100 * [0]
    final_value_lst = 500 * [24000]
    step_lst = initial_val_lst + final_value_lst
    for value in step_lst:
        encoderPosSpeed = encoder1.read()
        controller1.set_setpoint(value)
        controller1.run(encoderPosSpeed[0])


if __name__ == '__main__':
    main()
