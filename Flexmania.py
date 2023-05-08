import setup
def setupIMU():
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

def read_Keypad():
 if keypad_1.is_pressed:
    return('mpu')
  elif keypad_1.is_pressed:
    return('arcade')
  elif keypad_1.is_pressed:
    return('joystick')
  elif keypad_1.is_pressed:
    return('none')
def write_LCD():
  
