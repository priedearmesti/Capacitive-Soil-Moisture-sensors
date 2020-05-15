#******************************************************************
# Final Project:  Communication between a pair of Capacitive Soil Moisture sensors and the raspberry pi
#
# Programmer: - Ismilsys Priede Armesto
#             - Adam Neel
#
# Due Date: NA
#
# EGRE 491, Spring 2020       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Python file that contains four classes. The sensor class which implement a small state machine to determine 
#              which sensor should update its value. Humidity class which update the status of the sensor from: Wet, Medium-Wet and Dry. 
#              Some other classes to archive the overall functionality of “Humidity” and “Sensor”.
#
# Input: none
#
# Output: none
#
#******************************************************************

import enum


# this class holds the states values of the sensor, it will be used by the Humidity class
class StatesType(enum.Enum):
    Idle = 1
    Wet = 2
    Medium_Wet = 3
    Dry = 4

# Enumerate class that will be used by the sensor class
class StateSensor(enum.Enum):
    s1 = 1
    s2 = 2

# This class determines which sensor will update its value. Small state machine
class sensor:
    def __init__(self):
        self.status =  StateSensor.s1

    def update_sensor(self):
        if (self.status == StateSensor.s1):
            self.status = StateSensor.s2
        else:
            self.status = StateSensor.s1


#Thi class update the status of the sensor: Wet, Medium-Wet and Dry
class humidity:

    def __init__(self):
        self.value= 0
        self.state = StatesType.Idle            # when an object is created, state= idle which means that it doesn't have status yet because no value have been read.
        
    def update_states(self, c):
        self.value = c                          # update value       
        if (c < 400 ):                          
            self.state = StatesType.Wet
        elif ((c < 500) and  (c >=400)):
            self.state = StatesType.Medium_Wet
        else:
            self.state = StatesType.Dry


    def get_state(self):
        return self.state
        
        
    def get_value(self):
        return self.value
        
        

