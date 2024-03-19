#!/usr/bin/env python3
from inchworm_control.ik import inverseKinematicsMQP
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from inchworm_control.msg import Tuple 
# from inchworm_control.scripts.movement_command import *
# for servo
import RPi.GPIO as GPIO
import time
from inchworm_control.lewansoul_servo_bus import ServoBus
from time import sleep 
from threading import Thread


class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.publisher_ = self.create_publisher(Float32, 'step_status', 10)
        self.subscription = self.create_subscription(
            String,
            'motor_command',
            self.listener_callback,
            10)
        self.subscription
            # subscription for Tuple coming from step_publisher
        self.subscription = self.create_subscription(
            Tuple,
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
        # 
        # init motor angles
        print(self.motor_1.pos_read(), self.motor_2.pos_read(), self.motor_3.pos_read(), self.motor_4.pos_read(), self.motor_5.pos_read())

        self.step_actions = {
            'STEP_FORWARD': self.step_forward_block,
            'STEP_LEFT': self.step_left,
            'STEP_RIGHT': self.step_right,
            'GRAB_UP_FORWARD': self.grab_up_forward, 
            'PLACE_FORWARD': self.place_forward,
            'STEP_FORWARD_BLOCK': self.step_forward_block,
            'STEP_LEFT_BLOCK': self.step_left_block,
            'STEP_RIGHT_BLOCK': self.step_right_block,
            'PLACE_FORWARD_BLOCK': self.place_forward_block
            # Add more mappings as needed
        }

    def listener_callback(self, msg):
        self.get_logger().info('Received command to "%s' % msg.data)

        try:
            # self.grab_up_forward(1)
            # self.lift_block(1)
            # self.step_left()
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,4,1)
            theta4 += 20
            activate_servo(self.servo1)
            self.move_to(theta2, theta3, theta4, self.time_to_move)
            action = self.step_actions.get(msg.data)

            # print(msg.data)
            # # action = self.step_actions.get(step)
            
            # if action:
            #     action()
            # else:
            #     self.get_logger().warn('Unknown command: %s' % msg.data)
            
            # # publish step status. 0.0 means step sucessful, 1.0 means step error
            # msg = Float32()
            # msg.data = 0.0
            # self.publisher_.publish(msg)
            # self.get_logger().info('Publishing: "%s"' % msg.data)
            
        except Exception as e:
            self.get_logger().error('Failed to move servo: "%s"' % str(e))

    def init_motors(self):
        self.motor_1 = self.servo_bus.get_servo(1)
        self.motor_2 = self.servo_bus.get_servo(2)
        self.motor_3 = self.servo_bus.get_servo(3)
        self.motor_4 = self.servo_bus.get_servo(4)
        self.motor_5 = self.servo_bus.get_servo(5)

        self.time_to_move = 3

    def move_to(self, theta2, theta3, theta4, time):
        self.motor_2.move_time_write(theta2, time)
        self.motor_3.move_time_write(theta3, time)
        self.motor_4.move_time_write(theta4, time)
        sleep(time)
    
    # def move_to(self, tt2, tt3, tt4, time):
    #     print("move to")
    #     threshold = 5
    #     self.motor_2.move_time_write(tt2, time)
    #     while not self.is_within_range(self.motor_2.pos_read(), tt2, threshold):
    #         sleep(0.01)
    #         pass
    #     print('theta2 done')
    #     print('theta3', self.motor_3.pos_read())
    #     self.motor_3.move_time_write(tt3, time)

    #     while not self.is_within_range(self.motor_3.pos_read(), tt3, threshold):
    #         pass
    #     self.motor_4.move_time_write(tt4, time)
    #     while not self.is_within_range(self.motor_4.pos_read(), tt4, threshold):
    #         pass
    def is_within_range(self, current_pos, target_pos, threshold):
        if abs(current_pos - target_pos) <= threshold:
            return True
        else: return False

    # STEP DEFINITIONS 
    def step_forward(self):
        activate_servo(self.servo1)
        release_servo(self.servo2)
        # move up
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,2,1)
        theta4 += 20
        self.move_to(theta2, theta3, theta4, self.time_to_move)
        
        # move forward
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,3,1)
        # theta4 += 20
        self.move_to(theta2, theta3, theta4, self.time_to_move)

        # move down
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,0,1)
        # theta4 += 0
        self.move_to(theta2, theta3, theta4, self.time_to_move)
        print("before next servo command")
        activate_servo(self.servo2)
      
        ## following leg
        # Take the step up 
        release_servo(self.servo1)
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,2,5)
        theta2 -= 30
        self.move_to(theta2, theta3, theta4, self.time_to_move)

        # Take the step forward
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,3,5)
        theta2 -= 20
        self.move_to(theta2, theta3, theta4, self.time_to_move)

        # Get ready to put the step down 
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,0,5)
        self.move_to(theta2, theta3, theta4, self.time_to_move)
        activate_servo(self.servo1)
  
    def step_forward_wide(self):
        print('stepping forward wide')
        release_servo(self.servo2)

        ##move first 
        # move up
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,4,1)
        theta4 += 20
        activate_servo(self.servo1)
        self.move_to(theta2, theta3, theta4,self.time_to_move)
        # print('motor4 pose', theta4)
        
        # move forward
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(9,0,3,1)
        theta4 += 20
        self.move_to(theta2, theta3, theta4,self.time_to_move)
        # print('motor4 pose', theta4)


        # move down
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(9,0,0,1)
        theta4 += 0
        self.move_to(theta2, theta3, theta4,self.time_to_move)
        activate_servo(self.servo2)
      
        ## following leg
        # Take the step up 
        # release_servo(self.servo1)
        # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(9.2,0,4,5)
        # theta2 -= 30
        # self.move_to(theta2, theta3, theta4,self.time_to_move)

        # # Take the step forward
        # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.6,0,2,5)
        # theta2 -= 20
        # self.move_to(theta2, theta3, theta4,self.time_to_move)

        # # Get ready to put the step down 
        # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.6,0,0,5)
        # self.move_to(theta2, theta3, theta4,self.time_to_move)
        # activate_servo(self.servo1)
  
    def step_left(self):
        # still needs testing
        print('stepping left')
        release_servo(self.servo2)
        activate_servo(self.servo1)
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,3,1)
        theta4 += 20
        # theta5 += 40
        print("theta values", theta2, theta3, theta4)
        self.move_to(theta2, theta3, theta4, self.time_to_move)

        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,3,3,1)
        theta3 -= 10
        print("theta values", theta2, theta3, theta4)
        self.move_to(theta2, theta3, theta4, self.time_to_move)
        release_servo(self.servo2)

        # Rotate just the end-effector
        # self.move_to(theta1, theta2, theta3, theta4, (theta5-60))
        self.motor_1.move_time_write(theta1, self.time_to_move)
        self.motor_5.move_time_write(theta5-60, self.time_to_move)

        # mid-step allign
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.2,3.2,1,1)
        self.move_to(theta2, theta3, theta4, self.time_to_move)

        # Place the EE to final pose 
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.2,3.2,0,1)
        self.move_to(theta2, theta3, theta4, self.time_to_move)
        activate_servo(self.servo2)

        print("first part done")
        ## Second leg from here 
        release_servo(self.servo1)
        sleep(1)
        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.2,-3.2,3,5)
        theta2 -= 30
        self.move_to(theta2, theta3, theta4, self.time_to_move)

        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.1,0,3,5)
        self.motor_1.move_time_write(theta1, self.time_to_move)
        self.motor_5.move_time_write(theta5, self.time_to_move)

        theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,0,5)
        self.move_to(theta2, theta3, theta4, self.time_to_move)
        activate_servo(self.servo1)

    def step_right(self):
        pass

    def grab_up_forward(self, foot):

        print('grabbing up forward')

        #If foot 1, base is motor 1 
        if foot == 1: 
            release_servo(self.servo2)
            # move up
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,1,1)
            theta4 += 10
            print("theta4: ", theta4)
            # theta4 += 20
            activate_servo(self.servo1)
            self.move_to(theta2, theta3, theta4, 1)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,2,1)
            theta4 += 20
            print("theta4: ", theta4)
            self.move_to(theta2, theta3, theta4, 1)

            #move up more
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,6,1)
            theta4 += 20
            print("theta4: ", theta4)
            # print(theta2)
            self.move_to(theta2, theta3, theta4, 1)

            # move above block
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.25,0,5,1)
            # theta4 += 10
            self.move_to(theta2, theta3, theta4, self.time_to_move)

            # move on top block
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.25,0,2.75,1)
            # theta4 += 10
            self.move_to(theta2, theta3, theta4, self.time_to_move)
            activate_servo(self.servo2)

        # If foot 5, base is motor 5
        elif foot == 5:
            release_servo(self.servo1)
            # move up
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,1,5)
            print("theta2: ", theta2)
            # theta4 += 20
            activate_servo(self.servo2)
            self.move_to(theta2, theta3, theta4, 1)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,2,5)
            theta2 -= 20
            self.move_to(theta2, theta3, theta4, 1)

            #move up more
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,5,5)
            theta2 -= 20
            print(theta2)
            self.move_to(theta2, theta3, theta4, 1)

            # move above block
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.1,0,5,5)
            theta2 -= 20
            self.move_to(theta2, theta3, theta4, self.time_to_move)

            # move on top block
            #138.24 177.84 133.68 96.0 147.12
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.1,0,3,5)
            print(theta2, theta3, theta4)
            # theta4 += 10
            # self.move_to(177.84, 138.68, 96, self.time_to_move)
            self.move_to( theta2, theta3, theta4, self.time_to_move)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(7,0,3.05,5)
            print(theta2, theta3, theta4)
            # theta4 += 10
            # self.move_to(177.84, 138.68, 96, self.time_to_move)
            self.move_to( theta2, theta3, theta4, self.time_to_move)

            # Force it 
            # sleep(1)
            activate_servo(self.servo1)
            # sleep(1)
            

            release_servo(self.servo1)
            # self.servo1.ChangeDutyCycle(2+(90/18))
            # time.sleep(0.5)
            # self.servo1.ChangeDutyCycle(0)

            # release_servo(self.servo1)
            # sleep(1)
            activate_servo(self.servo1)

            # 
            release_servo(self.servo2)

            # move back leg in
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,0,1)
            # theta4 += 10
            self.move_to(theta2, theta3, theta4, self.time_to_move)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,0,1)
            # theta4 += 10
            self.move_to(theta2, theta3, theta4, self.time_to_move)

            # move back leg in
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3,0,-3.2,1)
            # theta4 += 10
            self.move_to(theta2, theta3, theta4, self.time_to_move)
            activate_servo(self.servo2)



        else:
            ValueError('are you stupid there is only 1 and 5????')

        #TODO
        #second foot should move in

    def lift_block(self,foot):
        if foot == 1:
            activate_servo(self.servo2)
            # theta4 = self.motor_4.pos_read()
            # self.motor_4.move_time_write(theta4+35, self.time_to_move)

            theta2 = self.motor_2.pos_read()
            self.motor_2.move_time_write(theta2-50, self.time_to_move)
            print(theta2)
            sleep(self.time_to_move)

            print("done moving theta2")
            theta3 = self.motor_3.pos_read()
            print(theta3)
            self.motor_3.move_time_write(theta3-50, self.time_to_move)
            sleep(self.time_to_move)

            # move up 
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(4,0,6,1)
            self.move_to(theta2, theta3, theta4, self.time_to_move)
            print("done moving")

            # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,6,1)
            # self.move_to(theta2, theta3, theta4, self.time_to_move)


        elif foot == 5:
            pass

    def place_forward(self):
        pass

    def step_forward_block(self, foot):
        print('stepping forward with block')

        #If foot 1, base is motor 1 
        if foot == 1: 
            pass 

        # If foot 5, base is
        elif foot == 5:
            ##move first 
            # move up
            # this first part currently does not act well because the servo does not fully actuate and the leg gets caught on the other leg
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,4,5)
            theta4 += 20
            activate_servo(self.servo1)
            self.move_to(theta2, theta3, theta4,self.time_to_move)

            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6,0,6,5)
            # theta4 += 20
            activate_servo(self.servo1)
            self.move_to(theta2, theta3, theta4,self.time_to_move)
            
            # move forward
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(9,0,6,5)
            #theta4 += 40
            self.move_to(theta2, theta3, theta4,self.time_to_move)

            # move down
            theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(9,0,4,5)
            #theta4 += 20
            self.move_to(theta2, theta3, theta4,self.time_to_move)
            activate_servo(self.servo2)
        
            # ## following leg
            # # Take the step up 
            # release_servo(self.servo1)
            # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(6.2,0,0,5)
            # theta2 -= 30
            # self.move_to(theta2, theta3, theta4,self.time_to_move)

            # # Take the step forward
            # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.6,0,-1,5)
            # theta2 -= 20
            # self.move_to(theta2, theta3, theta4,self.time_to_move)

            # # Get ready to put the step down 
            # theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(3.6,0,-3,5)
            # self.move_to(theta2, theta3, theta4,self.time_to_move)
            # activate_servo(self.servo1)

        else:
            ValueError('are you stupid there is only 1 and 5????')

    def step_left_block(self):
        pass

    def step_right_block(self):
        pass

    def place_forward_block(self):
        pass

# servo angle of 0 is activated, 180 released
def activate_servo(servo_id):
    servo_id.ChangeDutyCycle(2+(0/18))
    time.sleep(0.7)
    servo_id.ChangeDutyCycle(0)

def release_servo(servo_id):
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