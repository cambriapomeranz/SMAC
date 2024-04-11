How to Control the Inchworm Robot

**We use two ROS nodes to run the inchworm: motor_controller.py and step_publisher.py.**
Motor_controller subscribes to string messages on the topic 'motor_command'. The string emssage indicates what step to execute. When a step is recieved, then the inchwormn executes the respective step and publishes a Float32 on the topic 'step_status'. Step_pulbisher subscribes to Float32 messages on the topic 'step_status'. When it recieves a 'step_status' messages, it is prompted to publish the next step in steps.txt as a String message on the topic 'motor_command'. The two nodes communicate back and forth as such until all the steps are executed. Step_publisher initiates this loop by publising the first step in steps.txt when the node instantiates. 
Note: The Float32 published by motor_controller.py is just 0.0 in all cases, but this should change when implementing some sort of error handling. 

**How to Create a New Move **
Please note that the inverse kinematics calculations only focus on the EE location of the inchworm NOT the orientation. Our demo didn’t require any situation for us to change the orientation of the inchworm. There is no motion planning integrated, instead we divide the desired step into multiple steps to avoid collision and use offsets on certain motors individually.

Following code block can be used to move the robot: The 4th variable indicates which leg of the robot is the base link. In this case we are using leg 5 as base link and the EE will be in x y z coordinates with respect to the base link. The move_to function sends commands to move each servo to the desired location with the 4th variable being the time to move. 

theta1, theta2, theta3, theta4, theta5 = inverseKinematicsMQP(0, 3, 3, 5)
self.move_to(theta2-10, theta3, theta4, 1)
 
**Known Errors **
“Expected header b'UU'; received header b' '.":
This issue indicates there is no communication (or improper communication) between the Pi and servos. The issue can be one of the followings: 
This issue might be caused by a timeout error. Go to the library and change the ServoBus class’ timeout variable to be at least 5.0 seconds. 
Check the wiring and see if everything is connected.
Make sure the TX and RX wires aren’t switched.
Make sure power is on!  
Make sure you can detect the TTL connector on the raspberryPi. If you want to make sure the TTL is working you can simply attach the TTL connector to your computer and see if the port is recognized. 
