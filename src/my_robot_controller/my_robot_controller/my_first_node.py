#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.counter = 0
        self.create_timer(1.0,self.timer_callback) # Create a timer that calls the callback every second


    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter)) # Log a message with the current counter value
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) # Keep the node running until it is shut down; need for the timer to work
    rclpy.shutdown()

if __name__ == '__main__':
    main()