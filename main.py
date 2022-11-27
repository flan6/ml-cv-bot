import os
import traceback
from time import time

import cv2
import numpy as np

from Detection import Detection
from WindowCapture import WindowCapture
from Vision import Vision

# initialize the WindowCapture class
wincap = WindowCapture('Albion Online Client')

# load an empty Vision class
vision = Vision()
# load an empty detection class
detector = Detection()

detector.start()
wincap.start()

loop_time = time()
while(True):
    try:
        # if we don't have a screenshot yet, don't run the code below this point yet
        if wincap.screenshot is None:
            continue
        # get an updated image of the game
        detector.update(wincap.screenshot)

        if not detector.rectangles:
            continue
        # draw the detection results onto the original image
        detection_image = vision.draw_rectangles(wincap.screenshot, detector.rectangles)
        # display the images
        cv2.imshow('Matches', detection_image)

        # debug the loop rate
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        # press 'q' with output window focused to exit.
        # waits 1 ms every loop to process key presses
        key = cv2.waitKey(1)
        if key == ord('q'):
            wincap.stop()
            detector.stop()
            cv2.destroyAllWindows()
            break
    except Exception as e:
        wincap.stop()
        detector.stop()
        cv2.destroyAllWindows()
        print("EXCEPTION")
        traceback.print_exc()
        break
