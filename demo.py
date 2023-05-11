import Flexmania
from threading import Thread, Lock, Event
from time import sleep
from queue import Queue


on_off_count = 0
start_stop_count = 0

blue_led = {
  0:1, 
  1:2,
  2:3,
  3:4,
  4:5,
  5:6,
  6:7,
  7:8,
  7,1
}
green_led = {
  8:2,
  9:3,
  10:4,
  11:5,
  12:6,
  13:7,
  13:4,
  15:8,
  15:3
}

enemy_blue_track = {
  5:6,
  7:1,
  7:8,
  6:7,
  3:4,
  0:1,
  1:2,
  2:3
}
enemy_green_track = {
  13:7,
  15:3,
  15:8,
  13:4,
  11:5,
  8:2,
  9:3,
  10:4
}



def enemy_move():
   while True:
      for (x,y), (x1, y2) in zip(enemy_blue_track.items(), enemy_green_track.items()):
        Flexmania.light_pixel(x, y, 255)
        Flexmania.light_pixel(x1, y1, 255)
        time.sleep(2)






def on_off_board():
  global on_off_count
  while True:
    if Flexmania.on_off() & ((on_off_count % 2) == 0 | on_off_count  == 0) :
      on_off_count += 1
      Flexmania.turn_on_board()
    else:
      on_off_count += 1
      Flexmania.turn_off_board()
  
def start_stop_board():
  global start_stop_count
  while True:
    if Flexmania.on_off() & ((start_stop_count % 2) == 0 | start_stop_count  == 0) :
      start_stop_count += 1
      Flexmania.start()
    else:
      start_stop_count += 1
      Flexmania.off()


def read_MPU():
  while True:
    x_axis = Flexmania.read_MPU6050('x')
    y_axis = Flexmania.read_MPU6050('y')
    return x_axis, y_axis
def read_arcade():
  while True:
    return(Flexmania.read_ArcadeButtons())
  
def update_score(score):
  while True:
    Flexmania.write_LCD(score)
def read_keypad():
  while True:
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




















