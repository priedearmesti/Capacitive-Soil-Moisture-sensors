#******************************************************************
# Final Project: Communication between a pair of Capacitive Soil Moisture sensors and the raspberry pi
#
# Programmer:  - Ismilsys Priede Armesto
#              - Adam Neel
#
# Due Date: NA
#
# EGRE 491, Spring 2020       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Python file that contains functions that will handler the GPIO port. 
#              Each led color have being assigned to a GPIO pin. 
#              Pins assignation have been done through two classes: “pin_sensor1” and “pin_sensor2” 
#
# Input: None
#
# Output: None
#
#******************************************************************//


from gpiozero import LED
from time import sleep


class pins_sensor1():
    green = LED(6)
    yellow = LED(22)
    red = LED(25)

class pins_sensor2():
    green = LED(26)
    yellow = LED(27)
    red = LED(23)

#-------------------------------------------------
# Functions to  show Sensor  status (light LEDs)
#------------------------------------------------

def ShowSensor1_wet():
    led = pins_sensor1()         # access to GPIO pins that have been assigned to Sensor 1
    led.red.off()
    led.yellow.off()
    led.green.on()

def ShowSensor1_medium():
    led = pins_sensor1()
    led.green.off()
    led.red.off()
    led.yellow.on()

def ShowSensor1_dry():
    led = pins_sensor1()
    led.green.off()
    led.yellow.off()
    led.red.on()

def ShowSensor2_wet():          # access to GPIO pins that have been assigned to Sensor 2
    led = pins_sensor2()
    led.red.off()
    led.yellow.off()
    led.green.on()

def ShowSensor2_medium():
    led = pins_sensor2()
    led.red.off()
    led.green.off()
    led.yellow.on()

def ShowSensor2_dry():
    led = pins_sensor2()
    led.green.off()
    led.yellow.off()
    led.red.on() 



# All LEDs are off 
def everything_off():
    led1 = pins_sensor1()
    led2 = pins_sensor2()
    led1.red.off()
    led1.yellow.off()
    led1.green.off()
    led2.red.off()
    led2.yellow.off()
    led2.green.off()

# All LEDs are on
def everything_on():
    led1 = pins_sensor1()
    led2 = pins_sensor2()
    led1.red.on()
    led1.yellow.on()
    led1.green.on()
    led2.red.on()
    led2.yellow.on()
    led2.green.on()



