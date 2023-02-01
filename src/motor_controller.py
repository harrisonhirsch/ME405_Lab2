"""!
    @file                       motor_controller.py
    @brief                      This class implements
    @details                    This is a driver for 
                                
    @author                     Peyton Archibald
    @author                     Harrison Hirsch
    @date                       January 31, 2023
"""


class MotorController:
    """!
    @brief                      This class implements 
    @details                    This is a driver for 
    """

    def __init__(self, initial_Kp, initial_set_point):
        """!
            @brief              Constructs an controller object
            @details            Upon instantiation, the controller object 
            @param  en_pin      The
            @param  in1pin      The
            @param  in2pin      The  
        """  
        self.Kp = initial_Kp
        self.set_point = initial_set_point
        print("Creating a motor controller")
        
    def run(self, current_point):
        return self.Kp*(self.set_point - current_point)
    
    def set_setpoint(self, new_set_point):
        self.set_point = new_set_point
        pass
    
    def set_Kp(self, new_Kp):
        self.Kp = new_Kp
        pass
    
    def print_results(self, position_delta):
        pass

    def store_data(self):
        pass
