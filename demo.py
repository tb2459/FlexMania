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
player_change = 0
enemy_pos_track = 0


top = [0,1,2]
left = [0,3,6]
down = [6,7,8]
right = [2,5,8]

mpu_queue = Queue()
joystick_queue = Queue()
arcade_queue = Queue()
controller = Queue()

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


turn_on_board(blue_led)

def enemy_move():
    while True:   
        enemy_pos_track = 0 
        for key, value in zip(enemy_blue_track, enemy_green_track):
            for (x,y), (x2,y2) in zip(key.items(), value.items()): 
                if x and x2 == player_pos:
                    turn_off_board(blue_led, green_led)
                    sys.exit(0)
                else:
                    light_pixel(y[0], y[1], 0)
                    light_pixel(y2[0], y2[1], 0)
                    light_pixel(y[0], y[1], 127)
                    light_pixel(y2[0], y2[1], 127)
                    time.sleep(1)
                    light_pixel(y2[0], y2[1], 0)
                    light_pixel(y[0], y[1], 0)
                    light_pixel(y[0], y[1], 255)
                    if enemy_pos_track > 7:
                        enemy_pos_track = 0
                    else:
                        enemy_pos_track += 1
                    enemy_pos_track = int(x)

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
        elif controller.get() == "arcade":
            if arcade_queue.get() == 'up'  and (not(player_pos in top)):
                player_change = -3 
            elif arcade_queue.get() == 'down' and (not(player_pos in down)):
                player_change = 3
            elif arcade_queue.get() == 'left' and (not(player_pos in left)):
                player_change = -1
            elif arcade_queue.get() == 'right' and (not(player_pos in right)):
                player_change = 1
        elif controller.get() == 'joystick':
            if joystick_queue.get() == 'up'  and (not(player_pos in top) and (digitalValue_Pressure_Sensor3 < 300 and digitalValue_Pressure_Sensor4 < 300)):
                player_change = -3 
            elif joystick_queue.get() == 'down' and (not(player_pos in down) and (digitalValue_Pressure_Sensor3 < 300 and digitalValue_Pressure_Sensor4 < 300)):
                player_change = 3
            elif joystick_queue.get() == 'left' and (not(player_pos in left) and (digitalValue_Pressure_Sensor1 < 300 and digitalValue_Pressure_Sensor2 < 300)):
                player_change = -1
            elif joystick_queue.get() == 'right' and (not(player_pos in right) and (digitalValue_Pressure_Sensor1 < 300 and digitalValue_Pressure_Sensor2 < 300)):
                player_change = 1
        elif controller.get() == 'none':
           pass
        player_move(player_change)

def player_move(player_change, player_pos):
    global enemy_pos
    global score
    if player_change + player_pos == enemy_pos:
        turn_off_board(blue_led, green_led)
        sys.exit(0)
    else:
        org_x = green_led[player_pos][player_pos][0]
        org_y =green_led[player_pos][player_pos][1]
        org_x2 = blue_led[player_pos][player_pos][0]
        org_y2 = blue_led[player_pos][player_pos][1]
        light_pixel(org_x, org_y, 0)
        light_pixel(org_x2, org_y2, 255)
        player_pos += player_change
        new_x = green_led[player_pos][player_pos][0]
        new_y = green_led[player_pos][player_pos][1]
        new_x2 = blue_led[player_pos][player_pos][0]
        new_y2 = blue_led[player_pos][player_pos][1]
        light_pixel(new_x2, new_y2, 0)
        light_pixel(new_x, new_y, 255)
        score += 1
        Flexmania.update_scoreboard(score)

def read_MPU():
  while True:
    x_axis = read_MPU6050('x')
    y_axis = read_MPU6050('y')
    x_y = [x_axis, y_axis]
    mpu_queue.put(x_y)
    
def read_arcade():
  while True:
    arcade_queue.put(read_ArcadeButtons())
    
def read_joystick():
  while True:
    joystick_queue.put(read_joystick())
  
def read_keypad():
  while True:
    controller.put(keypad())


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

read_keypad_thread = Thread(target = read_keypad)
read_keypad_thread.start()





















