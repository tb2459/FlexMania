#This is the library setup for the driver 
import board
import busio
import time
from adafruit_is31fl3731.matrix import Matrix as Display
i2c = busio.I2C(board.SCL, board.SDA)
display = Display(i2c)


#This is the library setup for the MPU 6050
from mpu6050 import mpu6050
mpu = mpu6050(0x68)

