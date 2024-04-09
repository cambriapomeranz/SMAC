How to Control the Inchworm Robot

We use two ROS nodes to run the inchworm: motor_controller.py and step_publisher.py.
Motor_controller subscribes to string messages on the topic 'motor_command'. The string emssage indicates what step to execute. When a step is recieved, thew inchwormn execuites the respective step and publishesd a Float32 on the topic 'step_status;. Step_pulbisher subrisbes to Float32 messages on the topic 'step_status'. When it recieves a 'step_'status' messages, it is prompted to publish the next step in steps.txt as a String message on the topic 'motor_command'. The two nodes communicate back and forth as such untiul all the steps are executed. Step_publisher initiates this loop by publising the first step in steps.txt when the node instantiates. 
Note: The Float32 published by motor_controller.py is just 0.0 in all cases, but this should change when implementing some sort of error handling. 
