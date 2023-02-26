import setup
def setupIMU():
  pass
def setupLEDMatrix(X_position, Y_position, intensity): #This turns on an LED at a given position with a given intensity for two seconds and then turns it off
  setup.display.pixel(X_position, Y-position, intensity)
  setup.time.sleep(2)
  setup.display.fill(0)
def setupMPU6050(axis): #This prints the value at whichever selected axis
  print(accel_data[axis])

