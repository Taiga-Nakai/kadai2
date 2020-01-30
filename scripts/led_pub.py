#!/usr/bin/env python

import roslib
import rospy
import time
import wiringpi
import subprocess
from std_msgs.msg import String

if __name__ == '__main__':
    subprocess.check_call('gpio export 17 out' ,shell=True)

    rospy.init_node('led_pub')

    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
    io.pinMode(17,io.OUTPUT)
    
    pub = rospy.Publisher('MorsePulse', String, queue_size=10)
    
    while not rospy.is_shutdown():
        io.digitalWrite(17,0)
        time.sleep(0.1)
        print("pub: start!\n")

        io.digitalWrite(17,1)
        time.sleep(0.1)
        io.digitalWrite(17,0)
        time.sleep(0.3)
        print("pub: Short")
        io.digitalWrite(17,1)
        time.sleep(0.3)
        io.digitalWrite(17,0)
        time.sleep(0.3)
        print("pub: Long")
        io.digitalWrite(17,1)
        time.sleep(0.1)
        io.digitalWrite(17,0)
        time.sleep(0.1)
        print("pub: Short")
        pub.publish("NA")
        
        time.sleep(0.7)
        print("")

        io.digitalWrite(17,1)
        time.sleep(0.1)
        io.digitalWrite(17,0)
        time.sleep(0.3)
        print("pub: Short")
        io.digitalWrite(17,1)
        time.sleep(0.3)
        io.digitalWrite(17,0)
        time.sleep(0.3)
        print("pub: Long")
        io.digitalWrite(17,1)
        time.sleep(0.1)
        io.digitalWrite(17,0)
        time.sleep(0.3)
        print("pub: Short")
        io.digitalWrite(17,1)
        time.sleep(0.1)
        io.digitalWrite(17,0)
        time.sleep(0.1)
        print("pub: Long")
        pub.publish("KA")
        
        
        time.sleep(0.7)
        print("")
        
        
        io.digitalWrite(17,1)
        time.sleep(0.1)
        io.digitalWrite(17,0)
        time.sleep(0.3)
        print("pub: Short")
        io.digitalWrite(17,1)
        time.sleep(0.3)
        io.digitalWrite(17,0)
        time.sleep(0.3)
        print("pub: Long")
        pub.publish("I")

        time.sleep(0.7)
        print("")
