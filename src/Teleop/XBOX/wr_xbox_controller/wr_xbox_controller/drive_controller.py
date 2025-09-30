# The file that will handle the collection of data I guess?
import rclpy
import rclpy.node import Node
import std_msgs.msg import String
import pygame

# This is the publisher node that will send out the controller data
class ControllerHandler(Node):
    
    controllers = []

    #
    def __init__(self):
        # call the node constructor
        super().__init__("controler_handler")
        
        pygame.init()
        pygame.controller.init()

        this.controller = pygame.controller.Controller(0)
        this.controller.init()

        # IDK wtf thise does  
        self.publisher = self.create_publisher(String, "swerve", 10)
        
        # Set a event loop?
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    # Feedback look 
    def timer_callback(self):

        controller_data = {
                # Left joystick
                "left_x" : 0,
                "left_y" : 0,
                # Right joystick
                "right_y" : 0,
                "right_x" : 0
                # Left Trigger
                "left_trigger" : 0,
                # Right Trigger
                "right_trigger" : 0
        }

        # using pygame get events
        for event in pygame.event.get():
            # this will kill the pygame instance
            if event.type == pygame.QUIT:
                pass


            # this will handle the use button down
            if event.type == pygame.CONTROLLERBUTTONDOWN:
                #event.button
                pass
            
            # this will handle the use of button up
            if event.type == pygame.CONTROLLERBUTTONUP:
                #event.button
                pass
            
            # Analog stick / triggers
            if event.type == pygame.CONTROLLERAXISMOTION:
                #event.axis
                match eventAxis:
                    # We are going to match patterns to shit
                    case 0:

                        pass
                    case 1:

                        pass
                    case 2:
                pass
            
            # D-pad
            if event.type == pygame.JOYHATMOTION:
                #event.value (x,y)
                pass


        #how exactly do we public the data to the 

        




def main(args = None):
    # ROS2 init
    rclpy.init(args = args)
    
    

    #Start the node
    rclpy.spin(ControlHandler())

    #Cleans up automatically




if __name__ == "__main__":
    main()
