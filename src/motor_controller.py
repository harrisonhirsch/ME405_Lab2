"""!
    @file                       motor_controller.py
    @brief                      A universal proportional control algorithm
    @details                    This is a class that implements a basic proportional control algorithm. The difference
                                between a setpoint and current position is multiplied by a proportional gain value to
                                produce an output.
                                
    @author                     Peyton Archibald
    @author                     Harrison Hirsch
    @date                       February 7, 2023
"""


class MotorController:
    """!
    @brief                      A class for creating a proportional controller, initially for use with a DC motor
    @details                    This is a class that implements a basic proportional control algorithm. The difference
                                between a setpoint and current position is multiplied by a proportional gain value to
                                produce an output.
    """

    def __init__(self, initial_Kp, initial_set_point):
        """!
            @brief                      Constructs a controller object
            @details                    Upon instantiation, the controller object has a defined proportional gain and
                                        initial setpoint. It notifies the user that a motor controller is being created
            @param  initial_Kp          The proportional gain to be used
            @param  initial_set_point   The initial setpoint to aim for
        """  
        self.Kp = initial_Kp
        self.set_point = initial_set_point
        print("Creating a motor controller")

    def run(self, current_point):
        """!
            @brief                  Runs the proportional control algorithm
            @details                Subtracts the current point from the setpoint and multiplies it by the gain value.
            @param  current_point   The current position of the system
            @return                 The output of the control system. For a motor, it is a duty cycle to send to the
                                    motor driver
        """
        return self.Kp*(self.set_point - current_point)
    
    def set_setpoint(self, new_set_point):
        """!
            @brief                  Changes setpoint of the proportional control algorithm
            @details                Replaces the previously defined setpoint with a newly defined setpoint
            @param  new_set_point   The new setpoint of the system
        """
        self.set_point = new_set_point
        pass
    
    def set_Kp(self, new_Kp):
        """!
            @brief              Changes gain value of the proportional control algorithm
            @details            Replaces the previously defined gain with a newly defined gain
            @param  new_Kp      The new gain of the system
        """
        self.Kp = new_Kp
        pass

    def store_data(self, data_lst, time, position):
        dataPt = [time, position]
        data_lst.append(dataPt)
        return data_lst
