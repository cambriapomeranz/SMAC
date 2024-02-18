import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # or whatever message type you need


class MotorPublisher(Node):
    def __init__(self):
        super().__init__('motor_publisher')
        self.publisher_ = self.create_publisher(Float32, 'motor_status', 10)
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.logic = 1 

    def timer_callback(self):
        msg = Float32()

        # Your motor command logic goes here
        if self.logic == 1:
            msg.data = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.logic = 2  # Update the instance variable, not a local variable
        elif self.logic == 2:
            msg.data = 90.0
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.logic = 1  # Update the instance variable, not a l
        
def main(args=None):
    rclpy.init(args=args)
    motor_publisher = MotorPublisher()
    rclpy.spin(motor_publisher)
    motor_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

