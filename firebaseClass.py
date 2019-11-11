from firebase import firebase
from time import sleep
import asyncio

class FireB:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://iotfortme.firebaseio.com', None)


    def callback_get(self, response):
            with open('/dev/null', 'w') as f:
                f.write(response)
    
    def getTemprature(self):
        return self.firebase.get('/Temp', None)
    
    def setTempature(self, temp):
        self.firebase.put_async('/', '/Temp', temp, {'print': 'pretty'})
    
    def getLight(self):
        return self.firebase.get('/Light', None)
        
    def setLight(self, light):
        self.firebase.put('/', '/Light', light)

    def getTheHoledata(self):
        return self.firebase.get('/', None)

    def updateValue(self, value):
        self.firebase.put('/', '/Btnstate', value)