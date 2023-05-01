from PIL import ImageGrab
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('https://chromedino.com/ \n')
pyautogui.moveTo(x=400, y=335)
pyautogui.click()
pyautogui.press('space')

def isCollision(data):
    
    for i in range(750, 850):
        for j in range(280, 350):
            if not pyautogui.pixelMatchesColor(i, j, (400, 400, (83, 83, 83)), tolerance=50):
                print('pulando')     
                pyautogui.press('space')
                return
    return 

while True: 
    image = ImageGrab.grab().convert('L')        
    data = image.load()    
    isCollision(data)
    
    # image.show()
    # break     