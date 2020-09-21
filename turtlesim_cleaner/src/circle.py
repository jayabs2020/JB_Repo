#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def circle():

    #Starts a new node
    rospy.init_node('turtlebot_controller', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x=rospy.get_param('~r')
    vel_msg.angular.z = 1.0

# Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(10)

    # For the next 6 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(6):
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        # Testing our function
        circle()
    except rospy.ROSInterruptException:
        pass