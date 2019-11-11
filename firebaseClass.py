from firebase import firebase
from time import sleep
import asyncio

class FireB:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://iotfortme.firebaseio.com', None)


    def callback_get(self, response):
            with open('/dev/null', 'w') as f:
                f.write(response)
    
    async def getTemprature(self):
        return await self.firebase.get('/Temp', None)
    
    def setTempature(self, temp):
        self.firebase.put_async('/', '/Temp', temp, {'print': 'pretty'})
        #sleep(1)
        #print("posted")
    
    async def getLight(self):
        return await self.firebase.get('/Light', None)
        
    async def setLight(self, light):
        await self.firebase.put('/', '/Light', light)

    async def getTheHoledata(self):
        return await self.firebase.get('/', None)

    async def updateValue(self, value):
        await self.firebase.put('/', '/Btnstate', value)