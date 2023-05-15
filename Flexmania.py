import setup


def on_off_up_game(on_off):
  
def read_MPU6050(axis): #This prints the value at whichever selected axis
  accel_data = mpu.get_accel_data()
  return(accel_data[axis])
def read_ArcadeButtons():
  if up_button.is_pressed:
    return('up')
  elif down_button.is_pressed:
    return('down')
  elif left_button.is_pressed:
    return('left')
  elif right_button.is_pressed:
    return('right')
  
  
def read_joystick():
  if up_joy.is_pressed:
    return('up')
  elif down_joy.is_pressed:
    return('down')
  elif left_joy.is_pressed:
    return('left')
  elif right_joy.is_pressed:
    return('right')  

def on_off():
  if on_off.is_pressed:
    return True
def start_stop():
  if start_stop.is_pressed:
    return True
  
def turn_on_board(blue_led):
  #add code to light up all leds with character in center and 1 enemy in top right corner
  for items in blue_led:
    for x,y in items.items():
        if x == 4:
            display.pixel(12, 6, 255)
        elif x == 2:
            display.pixel(2, 3, 255)
            display.pixel(10, 4, 255)
        else:
            display.pixel(y[0], y[1], 255)
  
def turn_off_board(blue, green):
  #turn off all the leds and scoreboard
  lcd.clear()
  for item1, item2 in zip(blue, green):
    for (x,y), (x1, y2) in zip(item1.items(), item2.items()):
        display.pixel(y[0], y[1], 0)
        display.pixel(y2[0], y2[1], 0)

def light_pixel(x, y, number):
  display.pixel(x, y, number)
    
      
def start():
  #start making the enemy move and wait for signal from controller
  while True:
    

def stop():
  #stop the enemy and character
  
def read_keypad():
  if keypad_1.is_pressed:
    return('mpu')
  elif keypad_2.is_pressed:
    return('arcade')
  elif keypad_3.is_pressed:
    return('joystick')
  elif keypad_4.is_pressed:
    return('none')
  
def write_LCD(text):
  lcd.clear()
  lcd.message(text)
  
  
