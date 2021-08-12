import cv2
import numpy as np
from threading import Thread, Lock

from numpy.core.fromnumeric import size

class Detection:
    
    # threading properties
    stopped = True
    lock = None
    rectangles = []
    
    # properties
    screenshot = None
    net = None
    colors = None
    class_names = None
    confThreshold = 0.8
   
    def __init__(self):
        # create a thread lock object
        self.lock = Lock()
        #initialize our detection net
        self.net = cv2.dnn_DetectionModel('Models/Crop_Detection_Model/custom-yolov4-tiny-detector.cfg', 'Models/Crop_Detection_Model/custom-yolov4-tiny-detector_best.weights')
        self.net.setInputSize(704, 704)
        self.net.setInputScale(1.0 / 255)
        self.net.setInputSwapRB(True)

    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()
    
    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()
    
    def stop(self):
        self.stopped = True

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            if not self.screenshot is None:
                # do object detection on screenshot
                classes, confidences, boxes = self.net.detect(self.screenshot, self.confThreshold, nmsThreshold=0.4)

                # lock the thread while updating the results
                self.lock.acquire()
                self.rectangles = classes, confidences, boxes #rectangles[0] = classes, rectangles[1] = confidences, rectangles[2] = boxes
                self.lock.release()
    