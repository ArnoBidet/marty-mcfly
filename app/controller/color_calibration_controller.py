from app.model.marty import Marty

class ColorCalibrationController():
    def __init__(self):
        self.marty = Marty()

    def calibrate(self, color):
        self.marty.color_calibration(color)