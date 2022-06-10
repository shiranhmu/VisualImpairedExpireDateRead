#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess

power_button = 3

#ON/OFF
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(power_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(power_button, GPIO.FALLING)

#Scan
#GPIO.setwarnings(False)
#GPIO.setup(scan_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#button_state = GPIO.input(scan_button)
#if (GPIO.input(scan_button) == True):
#    subprocess.call("/home/pi/project/IndepanDate/sandbox.test_pre_process.py", shell=False)
    
#if (GPIO.input(scan_button) == True):
#    subprocess.call("/home/pi/project/IndepanDate/sandbox.test_pre_process.py", shell=False)


subprocess.call(['shutdown', '-h', 'now'], shell=False)


