'''
A firebase realtime database handler for the backed of TME Education board 
Made by TME Education Ethiopia 
'''

#Importing neccessary libraries 
from firebase import firebase
from time import sleep


class FireB:
    def __init__(self):
        #Constructor for the class
        #The URL will be changed with a coresponding dtabase URL for your database
        self.firebase = firebase.FirebaseApplication('https://iotfortme.firebaseio.com', None)

    
    def getTemprature(self):
        #Get a value in the database with an intity name "Temp" which can be changed to a corresponding value 
        return self.firebase.get('/Temp', None)
    
    def setTempature(self, temp):
        #This update an intity named "Temp" with a certain value which is passed the method
        self.firebase.put_async('/', '/Temp', temp, {'print': 'pretty'})
    
    def getLight(self):
        return self.firebase.get('/Light', None)
        
    def setLight(self, light):
        self.firebase.put('/', '/Light', light)

    def getTheHoledata(self):
        #This fetches the hole data under the database as a Json 
        return self.firebase.get('/', None)
