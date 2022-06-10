import RPi.GPIO as GPIO          #Import GPIO library
import time                      #Import time library
from subprocess import Popen
import functions


functions.play_audio(True, "/home/pi/Desktop/DateRecords/welcome.mp3")

p = 0
GPIO.setmode(GPIO.BOARD)         #Set GPIO pin numbering
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Enable input and pull up resistors
while True:
    input_state = GPIO.input(11) #Read and store value of input to a variable
    if input_state == False:     #Check whether pin is grounded
       print('Button Pressed')   #Print 'Button Pressed'
       if(not p):
          p = Popen(['python', '/home/pi/project/IndepanDate/sandbox/main2.py'])
          print('start proccess')
       else:
          pass
       time.sleep(0.3)           #Delay of 0.3s
    if input_state == True:
       if(not p):
         pass
       else:
         p.kill()
         p=0
         print('p killed')
       print('Button not Pressed')   #Print 'Button Pressed'
       time.sleep(0.3)           #Delay of 0.3s
