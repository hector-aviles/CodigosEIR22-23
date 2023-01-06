#!/usr/bin/env python3
"""
This node is intended to be used to code the resulting policy
after modeling and training the MDPs using ProbLog.
This node provides serveral functions to check if there are
other vehicles around the car and to execute the three
different behaviors: steady motion, follow and pass. 
"""
import math
import numpy
import rospy
import ros_numpy
from std_msgs.msg import Float64MultiArray, Empty, Bool
from sensor_msgs.msg import PointCloud2

def check_obstacle_north():
    return rospy.wait_for_message("/obstacle/north", Bool, timeout=1.0).data

def check_obstacle_north_west():
    return rospy.wait_for_message("/obstacle/north_west", Bool, timeout=1.0).data

def check_obstacle_west():
    return rospy.wait_for_message("/obstacle/west", Bool, timeout=1.0).data

def check_obstacle_south_west():
    return rospy.wait_for_message("/obstacle/south_west", Bool, timeout=1.0).data

def main():
    global pub_obs_N, pub_obs_NW, pub_obs_W, pub_obs_SW
    print("INITIALIZING OBSTACLE DETECTOR...")
    rospy.init_node("policy")
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        rate.sleep()
    

if __name__ == "__main__":
    try:
        main()
    except:
        rospy.ROSInterruptException
        pass

    

