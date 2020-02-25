#auto screenshots

import pyautogui
import time
# Sleep for 5 seconds to allow me to open book
time.sleep(5)
# Range can be changed depending on the number of pages
for i in range(1000):
# Turn page
     pyautogui.keyDown('right')
     pyautogui.keyUp('right')
# Take and save a screenshot
     pyautogui.screenshot('images/page_%d.pdf' % i)




# Отображение позиции курсора и RGB-цвета пикселя под ним

import pyautogui
print('Нажмите Ctrl-C для выхода.')
try:
    while True:
        # Получение и вывод координат курсора, а также RGB-цвета пикселя под ним
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
 
except KeyboardInterrupt:
    print('\nГотово.')
