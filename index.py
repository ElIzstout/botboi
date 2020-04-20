from pynput.mouse import Button,Controller
from pynput.keyboard import Key, Controller
from pynput import mouse
from pynput import keyboard
import time
import random

keyboards= Controller()
mouses = Controller()
character = 0
send = "hello"
i=0
class SpamSequence:
    'phrases'
    

    def __init__(self):
        
        self.sendval= []
        


    def addphrase(self,tosend,place):

        self.sendval.insert(place,tosend)
    def send(self,count):
        return self.sendval

t=0
print("10")
while t<=5:
    time.sleep(1)
    print('%i'%(t))
    t+=1

time.sleep(300)
while i<=150:
    typem = random.randint(5,8)
    wait= random.randint(301,400)
    print(typem)
    print(wait)
    if i%2==0:
        keyboards.type("-work")
        keyboards.press(keyboard.Key.enter)
        keyboards.release(keyboard.Key.enter)
        time.sleep(typem)
    keyboards.type("-tips")
    keyboards.press(keyboard.Key.enter)
    keyboards.release(keyboard.Key.enter)
    
    #if typem == 1:
    #    keyboards.type('N I C E')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 2:
    #    keyboards.type('nice')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 3:
    #    keyboards.type('nICe')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 4:
    #    keyboards.type('NICE')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 5:
    #    keyboards.type('Nouce')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 6:
    #    keyboards.type('NICE')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 7:
    #    keyboards.type('N I C E')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 8:
    #    keyboards.type('n i c e')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 9:
    #    keyboards.type('NiCe')
    #    keyboards.press(keyboard.Key.enter)
    #elif typem == 10:
    #    keyboards.type('nicE')
    #    keyboards.press(keyboard.Key.enter)

    i+=1
    time.sleep(wait)