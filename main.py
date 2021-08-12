from Detection import Detection
import cv2
import numpy as np
import os
from time import time
from WindowCapture import WindowCapture
from Vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Albion Online Client')

# load an empty Vision class
vision = Vision()
# load an empty Vision class
detector = Detection()

detector.start()
wincap.start()

loop_time = time()
while(True):

    # if we don't have a screenshot yet, don't run the code below this point yet
    if wincap.screenshot is None:
        continue
    # get an updated image of the game
    detector.update(wincap.screenshot)
    # do object detection
    #rectangles = cascade_limestone.detectMultiScale(screenshot)

    # draw the detection results onto the original image
    #detection_image = vision_limestone.draw_rectangles(screenshot, rectangles)

    # display the images
    #cv.imshow('Matches', detection_image)
    #cv.imshow('debug', screenshot)

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

print('Done.')