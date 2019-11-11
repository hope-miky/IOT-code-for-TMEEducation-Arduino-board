import firebaseClass
import serialconnector 
from time import sleep
import threading

class sendS:
    def __init__(self):
      self.fc = firebaseClass.FireB()
      self.sc = serialconnector.serialClass()
      self.tempVal = 0
      self.t1 = ""
      
    
    def main(self):
        
        self.tempVal = self.sc.getSerialData()
        #sleep(2)
        if len(self.tempVal)>1:
          print(self.tempVal)
          self.fc.setTempature(self.tempVal)
        return 0



if __name__ == '__main__':
    sd = sendS()
    while(1):
      sd.main()

