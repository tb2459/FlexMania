import setup
import Flexmania
from threading import Thread, Lock, Event
from time import sleep
from queue import Queue
import sys



on_off_count = 0
start_stop_count = 0
index_i = 0
index_k = 1
score = 0
enemy_loop = 0
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
  7:1
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
  {5:6},
  {7:1},
  {7:8},
  {6:7},
  {3:4},
  {0:1},
  {1:2},
  {2:3}
}
enemy_green_track = [
  {13:7},
  {15:3},
  {15:8},
  {13:4},
  {11:5},
  {8:2},
  {9:3},
  {10:4}
]




game_board = [[{0:0}, {1:0}, {2:0}],
              [{3:0}, {4:0}, {5:0}],
              [{6:0}, {7:0}, {8:0}]]
  #1 = point
  #2 = player
  #3 = enemy
enemy_board = [
  [{2:[0,2]}],
  [{5:[1,2]}],
  [{8:[2,2]}],
  [{7:[2,1]}],
  [{6:[2,0]}],
  [{3:[1,0]}],
  [{0:[0,0]}],
  [{1:[0,1]}]
]



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
    for (x,y) in zip(enemy_blue_track, enemy_green_track):
      for (key,value), (key1, value2) in zip(x.items(), y.items()):
        if !(check_player()):
          
          Flexmania.light_pixel(key, value, 255)
          Flexmania.light_pixel(key1, value1, 255)
          for item in enemy_board[x]:
            for key, value in item[0].items():
              game_board[(value[0])][(value[1])].update({key, 3})
        
          time.sleep(2)

def check_player(x):
  for item in enemy_board[x+1]:
    for key, value in item[0].items():
      if game_board[(value[0])][(value[1])][key] == 2:
        Flexmania.write_LCD("You lost", score)
        time.sleep(10)
        Flexmania.turn_off_board()
        sys.exit(0)
      else:
        return false
      

        
        
def on_off_board():
  while True:
    if Flexmania.on_off() & ((on_off_count % 2) == 0 | on_off_count  == 0) :
      on_off_count += 1
      Flexmania.turn_on_board()
      for row in game_board:
        for item in row:
          for i, y in item.items():
            if i == 4:
              item.update({4: 2})
            elif i == 2:
              item.update({2: 3})
            else:
              item.update({i, 1})
    else:
      on_off_count += 1
      Flexmania.turn_off_board()
      for row in game_board:
        for item in row:
          for i, y in item.items():
              item.update({i, 0})
  
def start_stop_board():
  while True:
    if Flexmania.on_off() & ((start_stop_count % 2) == 0 | start_stop_count  == 0) :
      start_stop_count += 1
      Flexmania.start()
      enemy_move()
      player_move()
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




















