import time
from neopixel import *
import copy

from colors import *
from blinking_eyes import BLINKING_EYES
from heart_eyes import HEART_EYES
from angry_eyes import ANGRY_EYES
from excited_eyes import EXCITED_EYES


class Led_Manager():
    #LED Configuration
    LED_COUNT = 256
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 128
    LED_INVERT = False
    LED_CHANNEL = 0
    
    FPS = 10
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
    
    def clear_and_show(self):
        for i in range(self.LED_COUNT):
            self.matrix.setPixelColor(i, Color(0,0,0))
        self.matrix.show()
        
    def clear(self):
        for i in range(self.LED_COUNT):
            self.matrix.setPixelColor(i, Color(0,0,0))

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
        reverse = copy.deepcopy(array)
        reverse.reverse()
        return reverse
        
    def blinking_eyes(self, color=W):
        self.print_array(BLINKING_EYES, color) 
        self.print_array(self.get_reverse(BLINKING_EYES), color)
        self.clear_and_show()
        
    def heart_eyes(self, color=R):
        self.print_array(HEART_EYES, color) 
        self.print_array(self.get_reverse(HEART_EYES), color)
        self.clear_and_show()
        
    def angry_eyes(self, color=R):
        self.print_array(ANGRY_EYES, color) 
        self.print_array(self.get_reverse(ANGRY_EYES), color)
        self.clear_and_show()
        
    def excited_eyes(self, color=W):
        self.print_array(EXCITED_EYES, color) 
        self.print_array(self.get_reverse(EXCITED_EYES), color)
        self.clear_and_show()
        
        
        

