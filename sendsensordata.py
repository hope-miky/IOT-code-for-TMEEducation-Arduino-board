import firebaseClass
import serialconnector 
from time import sleep

class sendS:
    def __init__(self):
      self.fc = firebaseClass.FireB()
      self.sc = serialconnector.serialClass()
      self.tempVal = 0
    
    def main(self):
        self.tempVal = self.sc.getSerialData()
        print(self.tempVal)
        self.fc.setTempature(self.tempVal)
        sleep(1)



if __name__ == '__main__':
    sd = sendS()
    while(1):
        sd.main()

