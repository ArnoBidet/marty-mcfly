from app.model.marty import Marty

class DirectionalArrowsController():
		marty = Marty()

		def __init__(self):
				pass

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