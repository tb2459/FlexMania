import setup


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





def setupIMU()
  :
  pass
def setupLEDMatrix(X_position, Y_position, intensity): #This turns on an LED at a given position with a given intensity for two seconds and then turns it off
  setup.display.pixel(X_position, Y_position, intensity)
  setup.time.sleep(2)
  setup.display.fill(0)
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
  
def turn_on_board():
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

def start():
  #start making the enemy move and wait for signal from controller

def stop():
  #stop the enemy and character
  
def read_Keypad():
 if keypad_1.is_pressed:
    return('mpu')
  elif keypad_1.is_pressed:
    return('arcade')
  elif keypad_1.is_pressed:
    return('joystick')
  elif keypad_1.is_pressed:
    return('none')
def write_LCD(text):
  lcd.clear()
  lcd.message(text)
  
  
