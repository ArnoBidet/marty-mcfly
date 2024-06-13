from app.model.marty import Marty

class ColorCalibrationController():
    def __init__(self):
        self.marty = Marty()

    def calibrate(self, color, nb_marty = 0):
        self.marty.color_calibration(color, nb_marty)
