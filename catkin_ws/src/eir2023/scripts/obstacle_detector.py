#!/usr/bin/env python3
"""
This node detect obstacles around the car using the lidar sensor.
Obstacles are detected only by counting the number of points inside 
a bounding box. Each BB defines a region around de car:
----------------|
North           | CAR
----------------|---------|--------------|
North-west |     West     | South West   |
-----------|--------------|--------------|
"""
import math
import numpy
import rospy
import ros_numpy
from std_msgs.msg import Float64MultiArray, Empty, Bool
from sensor_msgs.msg import PointCloud2

def callback_point_cloud(msg):
    xyz = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(msg)
    xyz = xyz[(xyz[:,2] > -1.6) & (xyz[:,2] < 0.5) ] #Filters points on floor and higher points
    obstacle_N  = xyz[(xyz[:,0] >  2.5) & (xyz[:,0] <   15) & (xyz[:,1] < 1.5) & (xyz[:,1] > -1.5)].shape[0] > 1000
    obstacle_NW = xyz[(xyz[:,0] >  4.5) & (xyz[:,0] <   15) & (xyz[:,1] < 5.0) & (xyz[:,1] >  1.5)].shape[0] > 1000
    obstacle_W  = xyz[(xyz[:,0] > -4.5) & (xyz[:,0] <  4.5) & (xyz[:,1] < 5.0) & (xyz[:,1] >  1.5)].shape[0] > 1000
    obstacle_SW = xyz[(xyz[:,0] >  -10) & (xyz[:,0] < -4.5) & (xyz[:,1] < 5.0) & (xyz[:,1] >  1.5)].shape[0] > 1000
    pub_obs_N .publish(obstacle_N )
    pub_obs_NW.publish(obstacle_NW)
    pub_obs_W .publish(obstacle_W )
    pub_obs_SW.publish(obstacle_SW)

def main():
    global pub_obs_N, pub_obs_NW, pub_obs_W, pub_obs_SW
    print("INITIALIZING OBSTACLE DETECTOR...")
    rospy.init_node("obstacle_detector")
    rospy.Subscriber('/point_cloud', PointCloud2, callback_point_cloud)
    pub_obs_N  = rospy.Publisher("/obstacle/north"     , Bool, queue_size=10)
    pub_obs_NW = rospy.Publisher("/obstacle/north_west", Bool, queue_size=10)
    pub_obs_W  = rospy.Publisher("/obstacle/west"      , Bool, queue_size=10)
    pub_obs_SW = rospy.Publisher("/obstacle/south_west", Bool, queue_size=10)
    rate = rospy.Rate(10)
    
    rospy.spin()
    

if __name__ == "__main__":
    try:
        main()
    except:
        rospy.ROSInterruptException
        pass

    

