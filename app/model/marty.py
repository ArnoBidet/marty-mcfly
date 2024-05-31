from asyncio import wait
from turtle import delay
import numpy as np
from martypy import Marty as realMarty
class Marty():
		def __new__(cls):
			if not hasattr(cls, 'instance'):
				cls.instance = super(Marty, cls).__new__(cls)
			return cls.instance
		
		def __init__(self):
			self.marty = None
			self.marty_ip = None
			self.marty_connected = False
			self.marty_status = None

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

		def stand_straight(self):
			print("stand_straight")

		def dance(self):
			print("dance")

		def celebrate(self):
			print("celebrate")

		def wave_left(self):
			print("wave_left")

		def wave_right(self):
			print("wave_right")

		def hello(self):
			print("hello")

		def shoot_right(self):
			print("shoot_right")

		def shoot_left(self):
			print("shoot_left")

		def connect_marty(self,ip):
			try:
				self.marty = realMarty("wifi", ip, blocking=False)
				self.marty_connected = True
				self.marty.dance()
				self.marty.close()
				return "success"
			except:
				self.marty = None
				self.marty_connected = False
				return "failed"
