import Flexmania
from threading import Thread, Lock, Event
from time import sleep
from queue import Queue

#This is a basic example of giving x,y coordinates for the matrix LED and then applying a certain level of intensity for that particular LED 
x = int(input("Which x coordinate would you like to choose?"))
y = int(input("Which x coordinate would you like to choose?"))
intensity = int(input("Choose a light intensity ranging from 0 and 255?"))
Flexmania.setupLEDMatrix(x,y,intensity)


def read_MPU():
  x_axis = Flexmania.read_MPU6050('x')
  y_axis = Flexmania.read_MPU6050('y')
  
def read_arcade():
  return(Flexmania.read_ArcadeButtons())
  
def update_score():
  
def read_keypad():
  return(Flexmania.read_Keypad())
  
def update_board():
  





read_MPU6050_thread = Thread(target = read_MPU)
read_MPU6050_thread.start()

read_arcade_thread = Thread(target = read_arcade)
read_arcade_thread.start()

update_score_thread = Thread(target = update_score)
update_score_thread.start()

read_keypad_thread = Thread(target = read_keypad)
read_keypad_thread.start()

read_MPU6050_thread = Thread(target = read_MPU)




















