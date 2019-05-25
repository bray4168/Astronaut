import time
from neopixel import *

from colors import *
from blinking_eyes import BLINKING_EYES


class Led_Manager():
    #LED Configuration
    LED_COUNT = 256
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 64
    LED_INVERT = False
    LED_CHANNEL = 0
    
    FPS = 5
    FRAME_RATE = 1.0 /FPS
    
    def __init__(self):        
        self.matrix = Adafruit_NeoPixel(self.LED_COUNT, 
                                       self.LED_PIN, 
                                       self.LED_FREQ_HZ,
                                       self.LED_DMA,
                                       self.LED_INVERT,
                                       self.LED_BRIGHTNESS,
                                       self.LED_CHANNEL)
        self.matrix.begin()
        self.matrix.setBrightness(self.LED_BRIGHTNESS)
    
    def clear(self):
        for i in range(self.LED_COUNT):
            self.matrix.setPixelColor(i, Color(0,0,0))
        self.matrix.show()


    def print_array(self, array, color=Color(255, 255, 255)):
        # Loop through the array and print the pictures to the leds
        for screen in array:
            i = 0
            for led in screen:
              if(led == 0 or led == N):
                  self.matrix.setPixelColor(i, N)
              elif(led == U):
                  self.matrix.setPixelColor(i, color)
              else:
                  self.matrix.setPixelColor(i, led)
              i += 1
            self.matrix.show()
            time.sleep(self.FRAME_RATE)
            self.clear()
        
        
    def get_reverse(self, array):
        reverse = array
        reverse.reverse()
        return reverse
        
    def blinking_eyes(self):
        self.print_array(BLINKING_EYES)
        self.print_array(self.get_reverse(BLINKING_EYES))
        self.clear()

