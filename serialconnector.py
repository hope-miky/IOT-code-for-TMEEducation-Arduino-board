import serial
from time import sleep
import asyncio

class serialClass:
    def __init__(self):
        self.boundrate = 9600
        self.val = ""
        self.ser = serial.Serial('/dev/ttyACM0',self.boundrate, timeout=None)
        #self.ser.close()

    def getSerialData(self):
        self.val = self.ser.readline().decode('utf-8', 'ignore')
        sleep(2)
        return self.val.rstrip()


