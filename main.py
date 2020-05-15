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
# Description: Python program that communicates with an Arduino board through serial communication.
#              The Arduino board sends data of two Moisture sensors to the pi. 
#              The pi will receive the data and It will store the values for each sensor. 
#              Two Leds arrays connected to the GPIO pins will display the status of both sensor:
#              Green color for dry, Yellow for Medium-wet, and Red for Dry. 
#
# Input: Data from the Arduino board
#
# Output: GPIO signal to light LEDs
#
#******************************************************************//



import serial
from time import sleep
from humidity_class import * 
from functions import * 

def main():

    uart= serial.Serial("/dev/ttyACM0", 9600)           # activiate serial communication through USB with the arduino board at the boundrate of 9600
    sensor1 = humidity()                                # sensor1 is an object of class "humidity" . Humidity class has as atributes the Moister levels
    sensor2 = humidity()                                # sensor2 is an object of class "humidity" 

    sensor_turn = sensor()                              # sensor_turn is an object of class "sensor" which include a state machine to determine which data corresponds to each sensor

    while True:
        y = uart.readline().decode('utf-8').rstrip()    # read data from the arduino board
        x = int (y)                                     # convert data from string to integer
        if (sensor_turn.status == StateSensor.s1):      # the sensor state machine will determine which sensor should update its value
            sensor1.update_states(x)                    # update sensor 1
            if (sensor1.state == StatesType.Wet):
                ShowSensor1_wet()
                print (f"Sensor 1 is wet {x} \n")
            elif (sensor1.state == StatesType.Medium_Wet):
                ShowSensor1_medium()
                print (f"Sensor 1 is Medium {x} \n")
            elif (sensor1.state == StatesType.Dry):	
                ShowSensor1_dry()
                print(f"Sensor 1 is dry {x} \n")
        else:    # turn of sensor 2
            sensor2.update_states(x)                    # update sensor 2
            if (sensor2.state == StatesType.Wet ):
                ShowSensor2_wet()
                print (f"Sensor 2 is Wet: {x} \n")
            elif (sensor2.state == StatesType.Medium_Wet):
                ShowSensor2_medium()
                print (f"Sensor 2 is Medium Wet: {x} \n")
            elif (sensor2.state == StatesType.Dry):
                ShowSensor2_dry()
                print (f"Sensor 2 is Dry: {x} \n")
        sensor_turn.update_sensor()             	# update sensor state machine to determine which sensor will get the next reading 


# CTROL + C execption 

try:
    main()
except KeyboardInterrupt:
    print ("Program ended, LEDs off")
# to show that program will end, all led will be ON for 3 second before everything is off
    everything_on()
    sleep(3)
    everything_off()


