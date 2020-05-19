from pynput.mouse import Button,Controller
from pynput.keyboard import Key, Controller
from pynput import mouse
from pynput import keyboard
import time
import random

keyboards= Controller()

with open('srcbee.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
print(data," start")

script = str.split(data)

i=0

t=0
print(len(script))

while t<=5:
    time.sleep(1)
    print('%i'%(t))
    t+=1

time.sleep(1);

while i in range(len(script)):
    print(script[i],i)
    keyboards.type(script[i])
    time.sleep(.5)
    keyboards.type(' \n')
    time.sleep(551)
    i+=1
