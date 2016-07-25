#!/usr/bin/env python
import time
import roslib; roslib.load_manifest('ur_driver')
import rospy
import numpy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']

client = 0

def move_repeated():
    jointVariable = numpy.loadtxt(open("trajforsim.csv","rb"), delimiter=",",skiprows=0)
    jointVelocity = numpy.loadtxt(open("velforsim.csv","rb"), delimiter=",",skiprows=0)

    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    
    d = 3.0
    g.trajectory.points = []
    for i in range(len(jointVariable)):
        g.trajectory.points.append(JointTrajectoryPoint(positions=jointVariable[i].tolist(),
                                  velocities=jointVelocity[i].tolist(), time_from_start=rospy.Duration(d)))
        d += 0.01
    client.send_goal(g)
    try:
        client.wait_for_result()
    except KeyboardInterrupt:
        client.cancel_goal()
        raise

def main():
    global client
    try:
        rospy.init_node("circleMotion", anonymous=True, disable_signals=True)
        client = actionlib.SimpleActionClient('follow_joint_trajectory', FollowJointTrajectoryAction)
        print "Waiting for server..."
        client.wait_for_server()
        print "Connected to server"
        move_repeated()

    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()
