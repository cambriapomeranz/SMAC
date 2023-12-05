from math import sin, cos, pi
# import time
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
# from rospy import sleep
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped

class StatePublisher(Node):
    def __init__(self):
        rclpy.init()
        super().__init__('state_publisher')

        qos_profile = QoSProfile(depth=10)
        self.joint_pub = self.create_publisher(JointState, 'joint_states', qos_profile)
        self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
        self.nodeName = self.get_name()
        self.get_logger().info("{0} started".format(self.nodeName))

        loop_rate = self.create_rate(30)
        angle1 = 0.
        angle2 = pi/2
        angle3 = 0.
        angle4 = pi/2
        angle5 = 0.

        angle2 += (76.5139-180)*(pi/180)
        angle3 += -153.0237*(pi/180)
        angle4 += (76.5139-180)*(pi/180)
                # time.sleep(1)


        # Define initial joint states (ch172.08ange these if your robot has a different initial pose)
        self.joint_states = {
            'iw_ankle_foot_bottom': angle1,
            'iw_beam_ankle_bottom': angle2,
            'iw_mid_joint': angle3,
            'iw_beam_ankle_top': angle4,
            'iw_ankle_foot_top': angle5
        }

        # Joints and their parent-child links
        self.joints = {
            'foot_to_root': ('iw_root', 'iw_foot_bottom'),
            'iw_ankle_foot_bottom': ('iw_foot_bottom', 'iw_ankle_bottom'),
            'iw_beam_ankle_bottom': ('iw_ankle_bottom', 'iw_beam_bottom'),
            'iw_mid_joint': ('iw_beam_bottom', 'iw_beam_top'),
            'iw_beam_ankle_top': ('iw_beam_top', 'iw_ankle_top'),
            'iw_ankle_foot_top': ('iw_ankle_top', 'iw_foot_top')
        }
        degree = pi / 180.0



        try:
            while rclpy.ok():
                rclpy.spin_once(self)

                # Update joint_state
                now = self.get_clock().now()
                joint_state = JointState()
                joint_state.header.stamp = now.to_msg()
                joint_state.name = list(self.joint_states.keys())
                joint_state.position = [angle1, angle2, angle3, angle4, angle5]
                self.joint_pub.publish(joint_state)

                # # Broadcast transforms for each joint
                # for joint, (parent_link, child_link) in self.joints.items():
                #     transform = TransformStamped()
                #     transform.header.stamp = now.to_msg()
                #     transform.header.frame_id = parent_link
                #     transform.child_frame_id = child_link
                #     # Example: Assuming static transforms (replace with actual values from your robot configuration)
                #     transform.transform.translati172.08on.x = 0.0
                #     transform.transform.translation.y = 0.0
                #     transform.transform.translation.z = 0.0
                #     transform.transform.rotation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)  # Identity quaternion
                #     self.broadcaster.sendTransform(transform)
                transform = TransformStamped()
                transform.header.stamp = now.to_msg()
                transform.transform.translation.x = 0.
                transform.transform.translation.y = 0.
                transform.transform.translation.z = 0.
                transform.transform.rotation = \
                    euler_to_quaternion(0, 0, 0) 
                
                # angle3+= pi/8
                

                # send command 
                # servo_1.move_time_write(172.08, time_to_move)
                # servo_2.move_time_write(202.08, time_to_move)
                # servo_3.move_time_write(65.28, time_to_move)

                # sleep(3)

                # servo_1.move_time_write(152.40, time_to_move)
                # servo_2.move_time_write(221.40, time_to_move)
                # servo_3.move_time_write(30.00, time_to_move)
                    # loop_rate.sleep()

        except KeyboardInterrupt:
            pass

def euler_to_quaternion(roll, pitch, yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
    return Quaternion(x=qx, y=qy, z=qz, w=qw)

def main():
    node = StatePublisher()

if __name__ == '__main__':
    main()