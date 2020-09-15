import board
import busio
import adafruit_ht16k33.segments

import datetime  
import pytz  
from time import sleep

# Create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)

# Create a display device
display = adafruit_ht16k33.segments.Seg14x4(i2c)

isColonOn = True   
while True: 
    # Get current time for give time zone
    current_time = datetime.datetime.now(pytz.timezone('Europe/Berlin'))  
            
    # Printing value of now
    hour = "{:02d}".format(current_time.hour) 
    minute = "{:02d}".format(current_time.minute)

    isColonOn = not isColonOn
    if isColonOn:
        time = hour + '.' + minute
    else:
        time = hour + minute
    
    display.print(time)

    # Rest for a while
    sleep(1)