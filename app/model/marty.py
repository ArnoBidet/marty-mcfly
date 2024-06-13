from asyncio import wait
from turtle import delay
import numpy as np
from martypy import Marty as realMarty
class Marty():
	_instance = None
	marties = [None,None]
	marties_ip = [None,None]
	marties_connected = [False,False]
	marties_status = [None,None]
	colors = {"black":0, "red":0, "green":0, "dark_blue":0, "light_blue":0, "yellow":0, "pink":0}
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Marty, cls).__new__(cls, *args, **kwargs)
		return cls._instance


	def go_forw(self, nb_marty=0):
		if(self.marties_connected[nb_marty]):
			self.marties[nb_marty].walk(1,'auto',0,40,1700);
		else:
			print("No marty connected")

	def go_back(self, nb_marty=0):
		self.marties[nb_marty].walk(1,'auto',0,-40, 1700);

	def turn_left(self, nb_marty=0):
		self.marties[nb_marty].sidestep("left")

	def turn_right(self, nb_marty=0):
		self.marties[nb_marty].sidestep("right")

	def go_forw_left(self, nb_marty=0):
		for i in range(4):
			self.marties[nb_marty].walk(1, 'auto', 16, 1, 1000)
		self.stand_straight()

	def go_forward_right(self, nb_marty=0):
		for i in range(4):
			self.marties[nb_marty].walk(1, 'auto', -16, 1, 1000)
		self.stand_straight()

	def stand_straight(self, nb_marty=0):
		if (self.marties[nb_marty].get_joint_position('left knee') or self.marties[nb_marty].get_joint_position('right knee')):
			self.marties[nb_marty].walk(1, 'auto', 0, 8, 1700)
		self.marties[nb_marty].stand_straight(750)
		print(self.colors)

	def dance(self, nb_marty=0):
		self.marties[nb_marty].dance()

	def celebrate(self, nb_marty=0):
		self.marties[nb_marty].celebrate()

	def wave_left(self, nb_marty=0):
		self.marties[nb_marty].wave("left")

	def wave_right(self, nb_marty=0):
		self.marties[nb_marty].wave("right")

	def hello(self, nb_marty=0):
		self.marties[nb_marty].hello()

	def shoot_right(self, nb_marty=0):
		self.marties[nb_marty].kick("right")

	def shoot_left(self, nb_marty=0):
		self.marties[nb_marty].kick("left")

	def hi(self, nb_marty=0):
		self.marties[nb_marty].stand_straight(200, blocking=False)
		self.marties[nb_marty].eyes(pose_or_angle=-20, move_time=100, blocking=False)
		self.marties[nb_marty].arms(left_angle=0, right_angle=120, move_time=200)
		self.marties[nb_marty].arms(left_angle=0, right_angle=0, move_time=200, blocking=False)
		self.marties[nb_marty].eyes(pose_or_angle=0, move_time=100)

	def connect_marty(self,ip, nb_marty=0):
		try:
			self.marties[nb_marty] = realMarty("wifi", ip, blocking=False)
			self.marties_connected[nb_marty] = True
			self.marties[nb_marty].get_ready()
			return "success"
		except:
			self.marties[nb_marty] = None
			self.marties_connected[nb_marty] = False
			return "failed"

	def disconnect_marty(self,nbMarty=0):
		if (self.marties_connected[nbMarty] == True):
			self.marties[nbMarty].close()
			self.marties[nbMarty] = None
			self.marties_connected[nbMarty] = False
			return "success"
		else:
			return "failed"

	def color_calibration(self, color:str, nbMarty=0):
		mean = 0
		for i in range(15):
			mean = mean + int(self.marties[nbMarty].get_color_sensor_hex('left'), 16)
		self.colors[color] = mean / 15

	def resolve(nb_marty):
		pass


