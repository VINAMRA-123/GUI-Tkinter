
import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return
    
def isCollide(data):
    if i in range(300,415) :
        if i in range(550,650):
             if data [i,j] < 100:
                 hit("up")
                 return True

    if i in range(300,415):
        if i in range(410,550):
             if data [i,j] <100:
                 hit("down")
                 return True
    return False

 
if __name__ == "__main__": 
    time.sleep(2)
    while True:
        ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        
        
    
        # if i range ():
        #      if j in range():
        #          data [i,j] <80