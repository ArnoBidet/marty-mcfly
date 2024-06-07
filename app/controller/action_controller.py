from app.model.marty import Marty

class ActionController():
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