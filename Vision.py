import cv2
import numpy as np

class Vision:

    class_names = None
    colors = None



    def __init__(self):
        # reading class names
        with open('Models/Crop_Detection_Model/crop_names.txt', 'r') as f:
            self.class_names = f.read().split('\n')

        # Get a different randomized colors for each of the classes
        self.colors = np.random.uniform(0, 255, size=(len(self.class_names), 3))

    # given a list of [x, y, w, h] rectangles returned by find(), convert those into a list of
    # [x, y] positions in the center of those rectangles where we can click on those found items
    def get_click_points(self, rectangles):
        points = []

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles[2]:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))

        return points

    # given a list of [x, y, w, h] rectangles and a canvas image to draw on, return an image with
    # all of those rectangles drawn
    def draw_rectangles(self, frame, rectangles):
       
        '''
        # these colors are actually BGR
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        
        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, lineType=line_type)
        '''
        classes, confidences, boxes = rectangles
        for classID, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
    
            # get corresponding class color and name
            color = self.colors[int(classID)]
            class_name = self.class_names[int(classID)]
            
            # confidence percentage to display
            final_confidence = '%.2f' % confidence

            label = str(class_name + final_confidence)

            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            left, top, widht, height = box
            top = max(top, labelSize[1])
            cv2.rectangle(frame, box, color, thickness=3)
            cv2.rectangle(frame, (left, top - labelSize[1]), (left + labelSize[0], top + baseLine), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

        return frame

    # given a list of [x, y] positions and a canvas image to draw on, return an image with all
    # of those click points drawn on as crosshairs
    def draw_crosshairs(self, haystack_img, points):
        # these colors are actually BGR
        marker_color = (255, 0, 255)
        marker_type = cv2.MARKER_CROSS

        for (center_x, center_y) in points:
            # draw the center point
            cv2.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

        return haystack_img

    def centeroid(self, point_list):
        point_list = np.asarray(point_list, dtype=np.int32)
        length = point_list.shape[0]
        sum_x = np.sum(point_list[:, 0])
        sum_y = np.sum(point_list[:, 1])
        return [np.floor_divide(sum_x, length), np.floor_divide(sum_y, length)]

'''
# reading class names
with open('Models/Crop_Detection_Model/crop_names.txt', 'r') as f:
    self.class_names = f.read().split('\n')

# Get a different randomized colors for each of the classes
self.colors = np.random.uniform(0, 255, size=(len(self.class_names), 3))

# draw boxes, class names and confidence on each detection
for classID, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
    
    #get corresponding class color and name
    color = colors[int(classID)]
    class_name = class_names[int(classID)]
    
    #confidence percentage to display
    final_confidence = '%.2f' % confidence

    label = str(class_name + final_confidence)

    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    left, top, widht, height = box
    top = max(top, labelSize[1])
    cv2.rectangle(frame, box, color, thickness=3)
    cv2.rectangle(frame, (left, top - labelSize[1]), (left + labelSize[0], top + baseLine), (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

# display and write on disk the processed image
cv2.imshow('test', frame)
cv2.imwrite('test.png', frame)

#wait for key q to be pressed to close all windows
key = cv2.waitKey(0)
if key == 'q':
    cv2.destroyAllWindows()
    
'''