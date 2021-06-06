#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
import keyboard

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

class JointPub(object):
    def __init__(self,getch):

        self.publishers_array = []
        self._joint_1_pub = rospy.Publisher('/robot_arm/joint_1_position_controller/command', Float64, queue_size=1)
        self._joint_2_pub = rospy.Publisher('/robot_arm/joint_2_position_controller/command', Float64, queue_size=1)
        self._joint_3_pub = rospy.Publisher('/robot_arm/joint_3_position_controller/command', Float64, queue_size=1)
        self._joint_4_pub = rospy.Publisher('/robot_arm/joint_4_position_controller/command', Float64, queue_size=1)
        
        self.publishers_array.append(self._joint_1_pub)
        self.publishers_array.append(self._joint_2_pub)
        self.publishers_array.append(self._joint_3_pub)
        self.publishers_array.append(self._joint_4_pub)


    def move_joints(self, joints_array):

        i = 0
        for publisher_object in self.publishers_array:
          joint_value = Float64()
          joint_value.data = joints_array[i]
          rospy.loginfo(str(joint_value))
          publisher_object.publish(joint_value)
          i += 1


    def start_loop(self, rate_value = 2.0):
        rospy.loginfo("Start Loop")
        # pos1 = [1.0,0.0,0.0,0.0]
        # pos2 = [1.0,1.0,0.0,0.0]
        # pos3 = [1.0,1.0,0.8,0.0]
        # pos4 = [1.0,1.0,1.0,-0.2]
        # pos5 = [0.0,0.0,0.0,0.0]
        # position = "pos1"


        j1=0.0
        j2=0.0
        j3=0.0
        j4=0.0
        
        rate = rospy.Rate(rate_value)

        while not rospy.is_shutdown():
          # if position == "pos1":
          #   self.move_joints(pos1)
          #   position = "pos2"
          # elif position == "pos2":
          #   self.move_joints(pos2)
          #   position = "pos3"
          # elif position == "pos3":
          #   self.move_joints(pos3)
          #   position = "pos4"
          # elif position == "pos4":
          #   self.move_joints(pos4)
          #   position = "pos5"
          # elif position == "pos5":
          #   self.move_joints(pos5)
          #   position = "pos1"

          # if keyboard.is_pressed('q'):
          #       self.move_joints(pos1)
          # if keyboard.is_pressed('a'):
          #       self.move_joints(pos2)
              
          x = getch()
          print(x)
          if x=='q': #Increase joint 1 by 0.1
                j1=j1+0.1
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          elif x=='w': #Decrease joint 1 by 0.1
                j1=j1-0.1
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          elif x=='e': #Increase joint 2 by 0.1
                j2=j2+0.1
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          elif x=='r': #Decrease joint 2 by 0.1
                j2=j2-0.1
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          elif x=='t': #Increase joint 3 by 0.1
                j3=j3+0.1
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          elif x=='y': #Decrease joint 3 by 0.1
                j3=j3-0.1
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          elif x=='a': #Grip
                j4=-0.2
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          elif x=='s': #Release
                j4=0.0
                pos = [j1,j2,j3,j4]
                self.move_joints(pos)
          rate.sleep()




if __name__=="__main__":
    rospy.init_node('joint_publisher_node')
    getch = _Getch()
    joint_publisher = JointPub(getch)
    rate_value = 4.0
    joint_publisher.start_loop(rate_value)
