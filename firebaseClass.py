from firebase import firebase
from time import sleep
import asyncio

class FireB:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://iotfortme.firebaseio.com', None)
        
    
    async def getTemprature(self):
        return await self .firebase.get('/Temp', None)
    
    def setTempature(self, temp):
        self.firebase.put('/', '/Temp', temp)
        sleep(2)
    
    async def getLight(self):
        return await self.firebase.get('/Light', None)
        
    async def setLight(self, light):
        await self.firebase.put('/', '/Light', light)

    async def getTheHoledata(self):
        return await self.firebase.get('/', None)

    async def updateValue(self, value):
        await self.firebase.put('/', '/Btnstate', value)