#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32 
from std_msgs.msg import  String

def chatter_callback(message):

    rospy.loginfo(rospy.get_caller_id() + " I heard %s", message.data)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("alex", Int32 , chatter_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
