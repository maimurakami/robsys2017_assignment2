#!/usr/bin/env python

import rospy
import time
import pigpio
from time import sleep

pi = pigpio.pi()
pi.set_mode(25, pigpio.OUTPUT)
pi.set_PWM_frequency(25, 50)
pi.set_PWM_range(25, 100)

try:
    d = 0
    r = 5
    while True:
        pi.set_PWM_dutycycle(25, d)
        sleep(0.1)
        d += r
        if d >= 100 or d <= 0:
            r *= -1

except KeyboardInterrupt:
    pass

pi.set_mode(25, pigpio.INPUT)
pi.stop()
