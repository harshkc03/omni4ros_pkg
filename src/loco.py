#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import time


######################################## DO N0T TOUCH THE FOLLOWING LINES #################################################
                                                                                                                   
rospy.init_node('vel_Publisher')																				      
f_l_pub = rospy.Publisher('/open_base/front_left_joint_velocity_controller/command', Float64, latch=True, queue_size=1)    
f_r_pub = rospy.Publisher('/open_base/front_right_joint_velocity_controller/command', Float64, latch=True, queue_size=1) 
b_l_pub = rospy.Publisher('/open_base/back_left_joint_velocity_controller/command', Float64, latch=True, queue_size=1) 
b_r_pub = rospy.Publisher('/open_base/back_right_joint_velocity_controller/command', Float64, latch=True, queue_size=1)   
																						                       
def motor_front_left(f_l_dir, speed):                                                                                      
	vel = Float64()                                                                                                
	if speed > 30:                                                                                                 
		f_l_vel = 30                                                                                                 
	else:             																							   
		f_l_vel = speed																							   
	if f_l_dir == 'cw':																							   
		vel = f_l_vel 																							   
	elif f_l_dir == 'ccw':																						   
		vel = -1 * f_l_vel 																						   
	elif f_l_dir == 'stop':																						   
		vel = 0																									   
	f_l_pub.publish(vel)																							   
																												   
def motor_front_right(f_r_dir, speed):																					   
	vel = Float64()																								   
	if speed > 30:                                                                                                 
		f_r_vel = 30                                                                                                 
	else:                                                                                                          
		f_r_vel = speed                                                                                              
	if f_r_dir == 'cw':                                                                                              
		vel = f_r_vel                                                                                                
	elif f_r_dir == 'ccw':                                                                                           
		vel = -1 * f_r_vel
	elif f_r_dir == 'stop':                                                                                           
		vel = 0                                                                                                   
	f_r_pub.publish(vel)                                                                                             
                                                                                                                   
def motor_back_left(b_l_dir, speed):                                                                                      
	vel = Float64()                                                                                                
	if speed > 30:                                                                                                 
		b_l_vel = 30                                                                                                 
	else:                                                                                                          
		b_l_vel = speed                                                                                              
	if b_l_dir == 'cw':                                                                                              
		vel = b_l_vel                                                                                                
	elif b_l_dir == 'ccw':                                                                                           
		vel = -1 * b_l_vel                                                                                           
	elif b_l_dir == 'stop':                                                                                          
		vel = 0                                                                                                    
	b_l_pub.publish(vel)   

def motor_back_right(b_r_dir, speed):                                                                                      
	vel = Float64()                                                                                                
	if speed > 30:                                                                                                 
		b_r_vel = 30                                                                                                 
	else:                                                                                                          
		b_r_vel = speed                                                                                              
	if b_r_dir == 'cw':                                                                                              
		vel = b_r_vel                                                                                                
	elif b_r_dir == 'ccw':                                                                                           
		vel = -1 * b_r_vel                                                                                           
	elif b_r_dir == 'stop':                                                                                          
		vel = 0                                                                                                    
	b_r_pub.publish(vel)                                                                                           
                                                                                                                   
####################################################################################################################


def main():

	while not rospy.is_shutdown():
		motor_front_left('ccw', 10)
		motor_front_right('cw', 10)

		motor_back_left('ccw', 10)
		motor_back_right('cw', 10)


if __name__ == "__main__":
	main()