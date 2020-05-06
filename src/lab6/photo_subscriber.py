#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys


bridge = CvBridge()


def callback(ros_image):
    global bridge

    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print e

    grayscale_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", grayscale_image)

    cv2.waitKey(10)


def main():
    rospy.init_node("photo_subscriber", anonymous=True)
    rospy.Subscriber("video_data", Image, callback)
    rospy.spin()


if __name__ == "__main__":
    main()
