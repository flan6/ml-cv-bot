import subprocess
from fastgrab import screenshot
from xdo import Xdo
from threading import Thread, Lock
import numpy


class WindowCapture:
    # threading properties
    stopped = True
    lock = None
    screenshot = None
    # properties
    win_location = [0, 0]
    win_size = [0, 0]
    w = 0
    h = 0
    window = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    x = Xdo()

    def __init__(self, window_name='Albion Online Client'):
        # create a thread lock object
        self.lock = Lock()
        # search for the window by provided name
        res = subprocess.run(["xdotool", "search", f"(.*?){window_name}"], capture_output=True)
        if res.stdout:
            self.window_id = int(res.stdout)
            print('Window found.')
        else:
            raise Exception(f'Window not found. {window_name}')

        # gets window properties values
        self.win_location = self.x.get_window_location(self.window_id)
        self.win_size = self.x.get_window_size(self.window_id)
        self.w = self.win_size[0]
        self.h = self.win_size[1]

    def get_screenshot(self):
        bbox = (self.win_location[0], self.win_location[1], self.win_size[0], self.win_size[1])
        self.x.activate_window(self.window_id)
        self.x.wait_for_window_active(self.window_id)

        # take a screen screenshot of the game window
        img = screenshot.Screenshot().capture(bbox)
        img = img[..., :3]
        img = numpy.ascontiguousarray(img)

        return img

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            # get an updated image of the game
            screenshot = self.get_screenshot()
            # lock the thread while updating the results
            self.lock.acquire()
            self.screenshot = screenshot
            self.lock.release()
