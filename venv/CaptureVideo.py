import cv2
from mss import mss
import numpy as np
import keyboard


def start():
    sct = mss()

    coordinates = {
        'top': 490,
        'left': 230,
        'width': 1660,
        'height': 300
    }

    with open('actions.csv', 'w') as csv:
        x = 0
        check=False
        while True:

            img = np.array(sct.grab(coordinates))

            img = cv2.Canny(img, threshold1=100, threshold2=200)

            if keyboard.is_pressed('t'):
                check=cv2.imwrite('./dataset/nothing/frame_{0}.jpg'.format(x), img)
                if check:
                    csv.write('0\n')
                    print("Nothing")
                    x += 1

            if keyboard.is_pressed('up_arrow'):
                check = cv2.imwrite('./dataset/jump/frame_{0}.jpg'.format(x), img)
                if check:
                    csv.write('1\n')
                    print('Jump write')
                    x += 1
