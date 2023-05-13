import setup


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

def on_off():
  if on_off.is_pressed:
    return True
def start_stop():
  if start_stop.is_pressed:
    return True
  
def turn_on_board(blue_led):
  #add code to light up all leds with character in center and 1 enemy in top right corner
  for x,y in blue_led.items():
    if x,y == 4,5:
      pixel.display(12, 6, 255)
      pixel.display(10, 4, 255)
    else:
      pixel.display(x, y, 255)
  
def turn_off_board():
  #turn off all the leds and scoreboard
  lcd.clear()
  for (x,y), (x1, y2) in zip(blue_led.items(), green_led.items()):
    pixel.display(x, y, 0)
    pixel.display(x1, y1, 0)

def light_pixel(x, y, number):
  pixel.display(x, y, number)
    
      
def start():
  #start making the enemy move and wait for signal from controller
  while True:
    

def stop():
  #stop the enemy and character
  
def read_Keypad():
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
  
  
