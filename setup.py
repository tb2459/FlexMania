#This is the library setup for the driver 
import board
import busio
import spidev
import RPi.GPIO as GPIO
import time, sys
from gpiozero import Button
import Adafruit_CharLCD as LCD
from adafruit_is31fl3731.matrix import Matrix as Display
i2c = busio.I2C(board.SCL, board.SDA)
display = Display(i2c)


GPIO.setmode(GPIO.BCM)

ADC_CH0=0b10000000
ADC_CH1=0b10010000
ADC_CH2=0b10100000
ADC_CH3=0b10110000
ADC_CH4=0b11000000
ADC_CH7=0b11110000

spi = spidev.SpiDev()
spi.open(0,1)
spi.mode = 0b00
spi.max_speed_hz = 1350000

readBytes = spi.xfer2([ADC_CH0, 0x00])
digitalValue_Pressure_Sensor1 = (((readBytes[0] & 0b11) << 8) | readBytes[1])

readBytes = spi.xfer2([ADC_CH1, 0x00])
digitalValue_Pressure_Sensor2 = (((readBytes[0] & 0b11) << 8) | readBytes[1])

readBytes = spi.xfer2([ADC_CH2, 0x00])
digitalValue_Pressure_Sensor3 = (((readBytes[0] & 0b11) << 8) | readBytes[1])

readBytes = spi.xfer2([ADC_CH3, 0x00])
digitalValue_Pressure_Sensor4 = (((readBytes[0] & 0b11) << 8) | readBytes[1])

readBytes = spi.xfer2([ADC_CH4, 0x00])
digitalValue_Potentiometer = (((readBytes[0] & 0b11) << 8) | readBytes[1])

readBytes = spi.xfer2([ADC_CH7, 0x00])
digitalValue_Potentiometer = (((readBytes[0] & 0b11) << 8) | readBytes[1])


#This is the library setup for the MPU 6050
from mpu6050 import mpu6050
mpu = mpu6050(0x68)

#Arcade Button setup
up_button = Button(20)
down_button = Button(26)
left_button = Button(13)
right_button = Button(8)

#Keypad setup
keypad_1 = Button(14)
keypad_2 = Button(15)
keypad_3 = Button(18)
keypad_4 = Button(19)

lcd_rs = 6
lcd_en = 5
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 22
lcd_backlight = 2


lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)







