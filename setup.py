#This is the library setup for the driver 
import board
import busio
import time
from adafruit_is31fl3731.matrix import Matrix as Display
i2c = busio.I2C(board.SCL, board.SDA)
display = Display(i2c)
