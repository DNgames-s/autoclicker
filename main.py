import time 
import keyboard
import mouse

isClicking = False



def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Кликер отключен')
    else:
        isClicking = True
        print('Кликер включен')
        


keyboard.add_hotkey('Alt + V', set_clicker)

while True:
    if isClicking:
        mouse.double_click(button = 'left')
        time.sleep(0.1)






