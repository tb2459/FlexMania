#This is the library setup for the driver 
import board
import busio
import time
from gpiozero import Button
from adafruit_is31fl3731.matrix import Matrix as Display
i2c = busio.I2C(board.SCL, board.SDA)
display = Display(i2c)


#This is the library setup for the MPU 6050
from mpu6050 import mpu6050
mpu = mpu6050(0x68)

#Arcade Button setup
up_button = Button(20)
down_button = Button(26)
left_button = Button(13)
right_button = Button(6)

