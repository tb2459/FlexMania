import setup
import Flexmania
from threading import Thread, Lock, Event
from time import sleep
from queue import Queue
import sys



on_off_count = 0
start_stop_count = 0

score = 0


player_pos = 4
enemy_pos = 2

top = [0,1,2]
left = [0,3,6]
down = [6,7,8]
right = [2,5,8]

mpu_queue = []
joystick_queue = []
arcade_queue = []
controller = []

blue_led = [
    {0:[0,1]}, 
    {1:[1,2]},
    {2:[2,3]},
    {3:[3,4]},
    {4:[4,5]},
    {5:[5,6]},
    {6:[6,7]},
    {7:[7,8]},
    {8:[7,1]}, 
]
green_led = [
    {0:[8,2]}, 
    {1:[9,3]},
    {2:[10,4]},
    {3:[11,5]},
    {4:[12,6]},
    {5:[13,7]},
    {6:[13,4]},
    {7:[15,8]},
    {8:[15,3]}, 
]

enemy_blue_track = [
    {2:[5,6]}, 
    {5:[7,1]},
    {8:[7,8]},
    {7:[6,7]},
    {6:[3,4]},
    {3:[0,1]},
    {0:[1,2]},
    {1:[2,3]}, 
]
enemy_green_track = [
    {2:[13,7]}, 
    {5:[15,3]},
    {8:[15,8]},
    {7:[13,4]},
    {6:[11,5]},
    {3:[8,2]},
    {0:[9,3]},
    {1:[10,4]}, 
]


mpu_queue = []
joystick_queue = []
arcade_queue = []


def enemy_move():
  enemy_pos_track = 0
  while True:    
    for (key, value), (key2, value2) in zip(enemy_blue_track[enemy_pos_track].items(), enemy_green_track[enemy_pos_track].items()):
      if key and key2 == player_pos:
        sys.exit()
      else:
        Flexmania.light_pixel(value[0], value[1], 0)
        Flexmania.light_pixel(value2[0], value2[1], 0)
        Flexmania.light_pixel(value[0], value[1], 127)
        Flexmania.light_pixel(value2[0], value2[1], 127)
        time.sleep(1)
        Flexmania.light_pixel(value2[0], value2[1], 0)
        Flexmania.light_pixel(value[0], value[1], 255)
        if enemy_pos_track > 7:
            enemy_pos_track = 0
        else:
            enemy_pos_track += 1
        enemy_pos = key
      
def read_controller():
    while True:
        player_change = 0
        if controller.get() == "mpu":
            if mpu_queue.get()[1] > 5 and (not(player_pos in top)):
                player_change = -3 
            elif mpu_queue.get()[1] < -5 and (not(player_pos in down)):
                player_change = 3
            elif mpu_queue.get()[0] < -5 and (not(player_pos in left)):
                player_change = -1
            elif mpu_queue.get()[0] > 5 and (not(player_pos in right)):
               player_change = 1
        elif controller == "arcade":
            if arcade_queue.get() == 'up'  and (not(player_pos in top)):
                player_change = -3 
            elif arcade_queue.get() == 'down' and (not(player_pos in down)):
                player_change = 3
            elif arcade_queue.get() == 'left' and (not(player_pos in left)):
                player_change = -1
            elif arcade_queue.get() == 'right' and (not(player_pos in right)):
                player_change = 1
        elif controller == 'joystick':
            if joystick_queue.get() == 'up'  and (not(player_pos in top)):
                player_change = -3 
            elif joystick_queue.get() == 'down' and (not(player_pos in down)):
                player_change = 3
            elif joystick_queue.get() == 'left' and (not(player_pos in left)):
                player_change = -1
            elif joystick_queue.get() == 'right' and (not(player_pos in right)):
                player_change = 1
        player_move(player_change)
      
def player_move(player_change):
    if player_change + player_pos == enemy_pos:
        sys.exit(0)
    else:
        org_x = green_led[player_pos][player_pos][0]
        org_y =green_led[player_pos][player_pos][1]
        org_x2 = blue_led[player_pos][player_pos][0]
        org_y2 = blue_led[player_pos][player_pos][1]
        Flexmania.light_pixel(org_x, org_y, 0)
        Flexmania.light_pixel(org_x2, org_y2, 255)
        player_pos =+ player_change
        new_x = green_led[player_pos][player_pos][0]
        new_y = green_led[player_pos][player_pos][1]
        new_x2 = blue_led[player_pos][player_pos][0]
        new_y2 = blue_led[player_pos][player_pos][1]
        Flexmania.light_pixel(new_x2, new_y2, 0)
        Flexmania.light_pixel(new_x, new_y, 255)
        score += 1
      
        
        
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
    x_y = [x_axis, y_axis]
    mpu_queue.append(x_y)
    
def read_arcade():
  while True:
    arcade_queue.append(Flexmania.read_ArcadeButtons())
    
def read_joystick():
  while True:
    joystick_queue.append(Flexmania.read_joystick())
  
def update_score(score):
  while True:
    Flexmania.write_LCD(score)
def read_keypad():
  while True:
    controller.append(Flexmania.read_keypad())



read_on_off_board_thread = Thread(target = on_off_board)
read_on_off_board_thread.start()

read_start_stop_board_thread = Thread(target = start_stop_board)
read_start_stop_board_thread.start()

read_MPU6050_thread = Thread(target = read_MPU)
read_MPU6050_thread.start()

read_arcade_thread = Thread(target = read_arcade)
read_arcade_thread.start()

read_joystick_thread = Thread(target = read_joystick)
read_joystick_thread.start()

update_score_thread = Thread(target = update_score)
update_score_thread.start()

read_keypad_thread = Thread(target = read_keypad)
read_keypad_thread.start()

read_MPU6050_thread = Thread(target = read_MPU)




















