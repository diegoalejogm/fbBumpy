__author__ = 'Diego'

from pyvirtualdisplay import Display as pyvd

class DisplayWrapper:


    def __init__(self):
        self.display = pyvd(visible=0, size=(800, 600))


    # Initializes and returns new display
    def start(self):
        self.display.start()

    def stop(self):
        self.display.stop()