#!/usr/bin/env python3
import numpy
import rospy
from std_msgs.msg import Empty
from controller import Supervisor

TIME_STEP = 10
robot = Supervisor()

def callback_start(msg):
    global start
    start = True

def main():
    global start
    print('Starting Controller Supervisor...')
    car_1 = robot.getFromDef('obstacle_north_west')
    car_2 = robot.getFromDef('obstacle_west')
    car_3 = robot.getFromDef('obstacle_south_west')
    p0_1 = car_1.getPosition()
    p0_2 = car_2.getPosition()
    p0_3 = car_3.getPosition()
    tf_1 = car_1.getField('translation')
    tf_2 = car_2.getField('translation')
    tf_3 = car_3.getField('translation')
    start = False
    rospy.init_node("supervisor_node")
    rospy.Subscriber("/start", Empty, callback_start)
    loop = rospy.Rate(1000/TIME_STEP)
    while robot.step(TIME_STEP) != -1 and not rospy.is_shutdown():
        if start:
            start = False
            car_1.setVelocity([6,0,0, 0,0,0])
            car_2.setVelocity([6,0,0, 0,0,0])
            car_3.setVelocity([6,0,0, 0,0,0])
        loop.sleep()
        
if __name__ == "__main__":
    try:
        main()
    except:
        pass

