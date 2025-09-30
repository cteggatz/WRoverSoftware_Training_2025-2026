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

        # IDK wtf thise does  
        self.publisher = self.create_publisher(String, "topic", 10)
        
        # Set a event loop?
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    # Feedback look 
    def timer_callback(self):
        # using pygame get events
        for event in pygame.event.get():
            if event.type == :

        




def main(args = None):
    # ROS2 init
    rclpy.init(args = args)
    
    

    #Start the node
    rclpy.spin(ControlHandler())

    #Cleans up automatically




if __name__ == "__main__":
    main()
