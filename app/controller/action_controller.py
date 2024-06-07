from app.model.marty import Marty


class ActionController:
    def __init__(self):
        self.marty = Marty()

    def on_b_stand_straight(self):
        self.marty.stand_straight()

    def on_b_dance(self):
        self.marty.dance()

    def on_b_celebrate(self):
        self.marty.celebrate()

    def on_b_wave_left(self):
        self.marty.wave_left()

    def on_b_wave_right(self):
        self.marty.wave_right()

    def on_b_hello(self):
        self.marty.hello()

    def on_b_shoot_right(self):
        self.marty.shoot_right()

    def on_b_shoot_left(self):
        self.marty.shoot_left()

    def on_b_forw_click(self):
        self.marty.go_forw()

    def on_b_back_click(self):
        self.marty.go_back()

    def on_b_left_click(self):
        self.marty.turn_left()

    def on_b_right_click(self):
        self.marty.turn_right()

    def on_b_forw_left_click(self):
        self.marty.go_forw_left()

    def on_b_forw_right_click(self):
        self.marty.go_forward_right()

    def hi(self):
        self.marty.hi()