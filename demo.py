import Flexmania
from threading import Thread, Lock, Event
from time import sleep
from queue import Queue

#This is a basic example of giving x,y coordinates for the matrix LED and then applying a certain level of intensity for that particular LED 
x = int(input("Which x coordinate would you like to choose?"))
y = int(input("Which x coordinate would you like to choose?"))
intensity = int(input("Choose a light intensity ranging from 0 and 255?"))
Flexmania.setupLEDMatrix(x,y,intensity)

on_off_count = 0
start_stop_count = 0

def on_off_board():
  global on_off_count
  While True:
    if Flexmania.on_off() & ((on_off_count % 2) == 0 | on_off_count  == 0) :
      on_off_count += 1
      Flexmania.turn_on_board()
    else:
      on_off_count += 1
      Flexmania.turn_off_board()
  
def start_stop_board():
  global start_stop_count
  While True:
    if Flexmania.on_off() & ((start_stop_count % 2) == 0 | start_stop_count  == 0) :
      start_stop_count += 1
      Flexmania.start)
    else:
      start_stop_count += 1
      Flexmania.off()


def read_MPU():
  x_axis = Flexmania.read_MPU6050('x')
  y_axis = Flexmania.read_MPU6050('y')
  
def read_arcade():
  return(Flexmania.read_ArcadeButtons())
  
def update_score(score):
  Flexmania.write_LCD(score)
def read_keypad():
  return(Flexmania.read_Keypad())
  
def update_board():
  



read_on_off_thread = Thread(target = on_off)
read_on_off_thread.start()

read_start_stop_thread = Thread(target = start_stop)
read_start_stop_thread.start()

read_MPU6050_thread = Thread(target = read_MPU)
read_MPU6050_thread.start()

read_arcade_thread = Thread(target = read_arcade)
read_arcade_thread.start()

update_score_thread = Thread(target = update_score)
update_score_thread.start()

read_keypad_thread = Thread(target = read_keypad)
read_keypad_thread.start()

read_MPU6050_thread = Thread(target = read_MPU)




















