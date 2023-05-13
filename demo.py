import setup
import Flexmania
from threading import Thread, Lock, Event
from time import sleep
from queue import Queue


on_off_count = 0
start_stop_count = 0
index_i = 0
index_k = 1
Green: {
  1:[0,1]
  2:[1,2]
  3:[2,3]
  4:[3,4]
  5:[4,5]
  6:[5,6]
  7:[6,7]
  8:[7,8]
  9:[7,1]
}
Blue: {
  10:[8,2]
  11:[9,3]
  12:[10,4]
  13:[11,5]
  14:[12,6]
  15:[13,7]
  16:[13,4]
  17:[15,8]
  18:[15,3]
}
 Points: 
  {
  1:[[0,1],[8,2]]
  2:[[1,2],[9,3]]
  3:[[2,3],[10,4]]
  4:[[3,4],[11,5]]
  5:[[4,5],[12,6]]
  6:[[5,6],[13,7]]
  7:[[6,7],[13,4]]
  8:[[7,8],[15,8]]
  9:[[7,1],[15,3]]
}
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












def joystick():
  while True:
    if((index_i == 0) and (index_k == 1)):
      if(setup.digitalValue_Pressure_Sensor1<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 3
        index_k = 4
        Flexmania.light_pixel(index_i,index_k,127)
      if(setup.digitalValue_Pressure_Sensor4<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 1
        index_k = 2
        Flexmania.light_pixel(index_i,index_k,127)
    elif((index_i == 1) and (index_k == 2)):
      if(setup.digitalValue_Pressure_Sensor1<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 4 
        index_k = 5
        Flexmania.light_pixel(index_i,index_k,127)
      if(setup.digitalValue_Pressure_Sensor4<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 2 
        index_k = 3
        Flexmania.light_pixel(index_i,index_k,127)
      if(setup.digitalValue_Pressure_Sensor2<300):
        setup.display.pixel(index_i,index_k,0)
        index_i = 0
        index_k = 1
        Flexmania.light_pixel(index_i,index_k,127)
     elif((index_i == 2) and (index_k == 3)):
      if(setup.digitalValue_Pressure_Sensor1<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 5
        index_k = 6
        Flexmania.light_pixel(index_i,index_k,127)
      if(setup.digitalValue_Pressure_Sensor2<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 1
        index_k = 2
        Flexmania.light_pixel(index_i,index_k,127)
     elif((index_i == 3) and (index_k == 4)):
      if(setup.digitalValue_Pressure_Sensor1<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 6 
        index_k = 7
        Flexmania.light_pixel(index_i,index_k,127)
      if(setup.digitalValue_Pressure_Sensor4<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 4 
        index_k = 5
        setup.display.pixel(index_i,index_k,127)
      if(setup.digitalValue_Pressure_Sensor3<300):
        Flexmania.light_pixel(index_i,index_k,0)
        index_i = 0
        index_k = 1
        Flexmania.light_pixel(index_i,index_k,127)
def enemy_move():
   while True:
      if
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




















