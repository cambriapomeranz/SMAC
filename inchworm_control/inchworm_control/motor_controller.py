#!/usr/bin/env python3
from inchworm_control.ik import inverseKinematicsMQP
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from inchworm_control.scripts.movement_command import *
# for servo
import RPi.GPIO as GPIO
import time

from inchworm_control.lewansoul_servo_bus import ServoBus
from time import sleep 

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.publisher_ = self.create_publisher(Float32, 'step_status', 10)
        self.subscription = self.create_subscription(
            String,
            'motor_command',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.servo_bus = ServoBus('/dev/ttyUSB0')  # /dev/ttyUSB0 is port for RP /dev/ttylUSB0 or USB1 for cambria(switches randomly)
        self.get_logger().info('Node starting')

        # init motors
        self.init_motors()

        # init servos
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        self.servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
        self.servo2 = GPIO.PWM(13,50) # pin 13 for servo1, pulse 50Hz
        self.servo1.start(0)
        self.servo2.start(0)
        # MOTOR CANNOT GO NEGATIVE  

        self.step_actions = {
            'STEP_FORWARD': self.step_forward,
            'STEP_LEFT': self.step_left,
            'STEP_RIGHT': self.step_right,
            'GRAB_UP_FORWARD': self.grab_up_forward, 
            'PLACE_FORWARD': self.place_forward
            # Add more mappings as needed
        }

    def listener_callback(self, msg):
        self.get_logger().info('Received command to "%s' % msg.data)

        try:
            # initial motor configs
            # print("initial motor configs")
            # print(self.motor_1.pos_read(), self.motor_2.pos_read(), self.motor_3.pos_read(), self.motor_4.pos_read(), self.motor_5.pos_read())
            release_servo(self.servo1)
            release_servo(self.servo2)

            # get and deploy next step
            action = self.step_actions.get(msg.data)
            if action:
                print(msg.data)
                action()
            else:
                self.get_logger().warn('Unknown command: %s' % msg.data)
            
            # publish step status. 0.0 means step sucessful, 1.0 means step error
            msg = Float32()
            msg.data = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            
        except Exception as e:
            self.get_logger().error('Failed to move servo: "%s"' % str(e))

    def init_motors(self):
        self.motor_1 = self.servo_bus.get_servo(1)
        self.motor_2 = self.servo_bus.get_servo(2)
        self.motor_3 = self.servo_bus.get_servo(3)
        self.motor_4 = self.servo_bus.get_servo(4)
        self.motor_5 = self.servo_bus.get_servo(5)

        self.time_to_move = 2

    def move_to(self, theta1, theta2, theta3, theta4):
        # print(theta1, theta2, theta3, theta4, theta5)
        self.motor_1.move_time_write(theta1, self.time_to_move)
        self.motor_2.move_time_write(theta2, self.time_to_move)
        self.motor_3.move_time_write(theta3, self.time_to_move)
        self.motor_4.move_time_write(theta4, self.time_to_move)
        # self.motor_5.move_time_write(theta5, self.time_to_move)
        sleep(2)

    # STEP DEFINITIONS 

    def step_forward(self):
        print('stepping forward')
        # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(0,0,2,1)
        # self.move_to(theta1, theta2, theta3, theta4)

        ##move first 
        # move up
        # this first part currently does not act well because the servo does not fully actuate and the leg gets caught on the other leg
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,4,1)
        theta4 += 20
        activate_servo(self.servo1)
        self.move_to(theta1, theta2, theta3, theta4)
        
        # move forward
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,3,1)
        theta4 += 20
        self.move_to(theta1, theta2, theta3, theta4)

        # move down
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,0,1)
        theta4 += 0
        self.move_to(theta1, theta2, theta3, theta4)
        activate_servo(self.servo2)
      
        ## following leg
        # Take the step up 
        release_servo(self.servo1)
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.2,0,4,5)
        theta2 -= 30
        self.move_to(theta1, theta2, theta3, theta4)

        # Take the step forward
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.6,0,2,5)
        theta2 -= 20
        self.move_to(theta1, theta2, theta3, theta4)

        # Get ready to put the step down 
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.6,0,0,5)
        self.move_to(theta1, theta2, theta3, theta4)
        activate_servo(self.servo1)

    def turn_left(self):
        print('stepping left')
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,3,1)
        theta4 += 50
        self.move_to(theta1, theta2, theta3, theta4)

        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,5,2,1)
        self.move_to(theta1, theta2, theta3, theta4)


    def step_left(self):
        print('stepping left')
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,3,1)
        theta4 += 50
        self.move_to(theta1, theta2, theta3, theta4)

        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,5,2,1)
        self.move_to(theta1, theta2, theta3, theta4)

    def step_right(self):
        pass

    def grab_up_forward(self):
        pass

    def place_forward(self):
        pass

# servo angle of 180 is activated, 0 released
def activate_servo(servo_id):
    servo_id.ChangeDutyCycle(2+(0/18))
    # print("servo activated")
    time.sleep(0.5)
    servo_id.ChangeDutyCycle(0)

def release_servo(servo_id):
    # print('Releasing')
    servo_id.ChangeDutyCycle(2+(180/18))
    time.sleep(0.5)
    servo_id.ChangeDutyCycle(0)

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()