import serial


class serialClass:
    def __init__(self):
        self.boundrate = 9600
        self.val = ""
        self.ser = serial.Serial('/dev/ttyACM0',self.boundrate, timeout=None)
        
    def getSerialData(self):
        self.val = self.ser.readline().decode('utf-8', 'ignore')
        return self.val.rstrip()


