#!/usr/bin/env python3

import time
from neopixel import *

from colors import *
from led_manager import Led_Manager

#LED Configuration
LED_COUNT = 256
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 64
LED_INVERT = False
LED_CHANNEL = 0

FPS = 5
FRAME_RATE = 1.0 / FPS

def clear(led_matrix):
    for i in range(LED_COUNT):
        led_matrix.setPixelColor(i, Color(0,0,0))
    led_matrix.show()

        
def print_array(led_matrix, array, color=Color(255, 255, 255)):
    # Loop through the array and print the pictures to the leds
    for screen in array:
        i = 0
        for led in screen:
          if(led == 0 or led == N):
              led_matrix.setPixelColor(i, N)
          elif(led == U):
              led_matrix.setPixelColor(i, color)
          else:
              led_matrix.setPixelColor(i, led)
          i += 1
        led_matrix.show()
        time.sleep(FRAME_RATE)
        clear(led_matrix)

if __name__ == '__main__':
    led_manager = Led_Manager()
    led_manager.blinking_eyes()
    
    
    
    
