#This is the library setup for the driver 
import board
import busio
import RPi.GPIO as GPIO
import time, sys
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
right_button = Button(8)


LCD_RS = 6
LCD_E = 5
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 22
LCD_CHR = GPIO.HIGH 
LCD_CMD = GPIO.LOW 

LCD_E_HI = 0.0005
LCD_E_LO = 0.0005

LCD_CMD_CLEAR  = 0b00000001 # clear display
LCD_CMD_DSPON  = 0b00001110 # display on, with cursor, no blinking
LCD_CMD_DSPOFF = 0b00001000 # display off
LCD_CMD_ENTRY  = 0b00000110 # entry mode set
LCD_CMD_FNSET  = 0b00101000 # function set, 4 bit operation, 2 lines, 5x8 font
LCD_CMD_4BIT   = 0b00110010 # change to 4 bit mode
LCD_CMD_RESET  = 0b00110000 # reset (as described in "Reset function")

def lcd_byte(bits, mode):
  # Set RS line to whatever we passed in "mode"
  GPIO.output(LCD_RS, mode)
  # Send high (leftmost) bits
  GPIO.output(LCD_D7, (bits >> 7) & 1)
  GPIO.output(LCD_D6, (bits >> 6) & 1)
  GPIO.output(LCD_D5, (bits >> 5) & 1)
  GPIO.output(LCD_D4, (bits >> 4) & 1)
  # Pulse "E" line
  GPIO.output(LCD_E, GPIO.LOW)
  time.sleep(LCD_E_LO)
  GPIO.output(LCD_E, GPIO.HIGH)
  time.sleep(LCD_E_HI)
  GPIO.output(LCD_E, GPIO.LOW)
  time.sleep(LCD_E_LO)
  # Send low (rightmost) bits
  GPIO.output(LCD_D7, (bits >> 3) & 1)
  GPIO.output(LCD_D6, (bits >> 2) & 1)
  GPIO.output(LCD_D5, (bits >> 1) & 1)
  GPIO.output(LCD_D4, (bits >> 0) & 1)
  # Pulse "E" line
  GPIO.output(LCD_E, GPIO.LOW)
  time.sleep(LCD_E_LO)
  GPIO.output(LCD_E, GPIO.HIGH)
  time.sleep(LCD_E_HI)
  GPIO.output(LCD_E, GPIO.LOW)
  time.sleep(LCD_E_LO)
  
def lcd_init():
  GPIO.setmode(GPIO.BCM)

  # Configure pins as outputs
  GPIO.setup(LCD_RS, GPIO.OUT)
  GPIO.setup(LCD_E, GPIO.OUT)
  GPIO.setup(LCD_D4, GPIO.OUT)
  GPIO.setup(LCD_D5, GPIO.OUT)
  GPIO.setup(LCD_D6, GPIO.OUT)
  GPIO.setup(LCD_D7, GPIO.OUT)
# Put display in 4-bit mode
  lcd_byte(LCD_CMD_RESET,  LCD_CMD)
  lcd_byte(LCD_CMD_RESET,  LCD_CMD)
  lcd_byte(LCD_CMD_4BIT,   LCD_CMD)

    # Run the rest of the initialization sequence
  lcd_byte(LCD_CMD_FNSET,  LCD_CMD)
  lcd_byte(LCD_CMD_DSPOFF, LCD_CMD)
  lcd_byte(LCD_CMD_CLEAR,  LCD_CMD)
  lcd_byte(LCD_CMD_ENTRY,  LCD_CMD)

    # Turn the display on
  lcd_byte(LCD_CMD_DSPON,  LCD_CMD)

def lcd_char(c):
    dec = ord(c)
    lcd_byte(dec, LCD_CHR)







