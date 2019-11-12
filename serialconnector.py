'''
This Class handles the serial communication with the Arduino board 
Made by TME Education Ethiopia 
'''

#Importing neccessary libraries 
import serial
from time import sleep


class serialClass:
    def __init__(self):
        #Constructor for the class
        self.boundrate = 9600               #Bound rate which is defined in the Arduino code 
        self.val = ""
        self.ser = serial.Serial('/dev/ttyACM0',self.boundrate, timeout=2)      #Defining an Object for the serial communication with a certain characteristics 


    def getSerialData(self):
        #Get serial data from the Arduino 
        self.val = self.ser.readline().decode('utf-8', 'ignore')        #Decode the recieved values to strings (utf-8)
        return self.val.rstrip()                                        #Remove the strip and return the value


