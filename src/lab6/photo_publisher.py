#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


bridge = CvBridge()
video_capture = cv2.VideoCapture("/home/osboxes/catkin_ws/src/"
                                 "robotika/videos/video.mp4")


def main():
    global bridge

    rospy.init_node("photo_publisher", anonymous=True)

    pub = rospy.Publisher("video_data", Image, queue_size=10)

    rate = rospy.Rate(22)

    while not rospy.is_shutdown():
        ret, frame = video_capture.read()

        frame = cv2.resize(frame, None, fx=0.2, fy=0.2)
        msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        pub.publish(msg)

        rate.sleep()


if __name__ == "__main__":
    main()
