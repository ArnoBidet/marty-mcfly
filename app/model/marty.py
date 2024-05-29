from random import randint
class Marty():
		def __new__(cls):
				if not hasattr(cls, 'instance'):
						cls.instance = super(Marty, cls).__new__(cls)
				return cls.instance
		
		def __init__(self):
				self.marty = None
				self.marty_ip = None
				self.marty_port = None
				self.marty_connected = False
				self.marty_status = None
				self.marty_status_text = None
				self.marty_status_color = None
				self.marty_status_icon = None
				self.marty_status_icon_color = None

		def go_forw(self):
				print("Button 'forward' clicked!")

		def go_back(self):
				print("Button 'backward' clicked!")

		def turn_left(self):
				print("Button 'left' clicked!")

		def turn_right(self):
				print("Button 'right' clicked!")

		def go_forw_left(self):
				print("Button 'forward-left' clicked!")

		def go_forward_right(self):
				print("Button 'forward-right' clicked!")