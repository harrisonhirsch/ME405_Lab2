import pyb
import motor_driver
import encoder_reader
import motor_controller

"""!
    @file                       main.py
    @brief                      Test
    @details                    This is .
                                
    @author                     Peyton Archibald
    @author                     Harrison Hirsch
    @date                       January 31, 2023
"""


def main():
    motor1 = motor_driver.MotorDriver('A10', 'B4', 'B5', 3)  # Set up motor 1
    encoder1 = encoder_reader.EncoderReader('C6', 'C7', 8)  # Set up encoder 1
    controller1 = motor_controller.MotorController(.1, 8000)  # Set up controller 1

    while True:
        try:
            encoderPosSpeed = encoder1.read()
            desiredDuty = controller1.run(encoderPosSpeed[0])
            print(desiredDuty, encoderPosSpeed[0])
            motor1.set_duty_cycle(desiredDuty)
        except KeyboardInterrupt:
            break
    motor1.set_duty_cycle(0)


if __name__ == '__main__':
    main()
