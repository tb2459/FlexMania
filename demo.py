import Flexmania
from threading import Thread, Lock, Event
from time import sleep
from queue import Queue


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
      Flexmania.start()
    else:
      start_stop_count += 1
      Flexmania.off()


def read_MPU():
  While True:
    x_axis = Flexmania.read_MPU6050('x')
    y_axis = Flexmania.read_MPU6050('y')
    return x_axis, y_axis
def read_arcade():
  While True:
    return(Flexmania.read_ArcadeButtons())
  
def update_score(score):
  While True:
    Flexmania.write_LCD(score)
def read_keypad():
  While True:
    return(Flexmania.read_Keypad())
  
def update_board():
  



read_on_off_board_thread = Thread(target = on_off_board)
read_on_off_board_thread.start()

read_start_stop_board_thread = Thread(target = start_stop_board)
read_start_stop_board_thread.start()

read_MPU6050_thread = Thread(target = read_MPU)
read_MPU6050_thread.start()

read_arcade_thread = Thread(target = read_arcade)
read_arcade_thread.start()

update_score_thread = Thread(target = update_score)
update_score_thread.start()

read_keypad_thread = Thread(target = read_keypad)
read_keypad_thread.start()

read_MPU6050_thread = Thread(target = read_MPU)




















