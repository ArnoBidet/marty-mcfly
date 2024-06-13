from asyncio import wait
from time import sleep
from turtle import delay
import numpy as np
from martypy import Marty as realMarty
class Marty():
	_instance = None
	marties = [None,None]
	marties_ip = [None,None]
	marties_connected = [None,None]
	marties_status = [None,None]
	labyrinth = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
	colors = {"black":0, "red":0, "green":0, "dark_blue":0, "light_blue":0, "yellow":0, "pink":0}
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Marty, cls).__new__(cls, *args, **kwargs)
		return cls._instance


	def go_forw(self, nbMarty=0):
		if(self.marties_connected[nbMarty]):
			self.marties[nbMarty].walk(1,'auto',0,35,1700)
		else:
			print("No marty connected")

	def go_back(self, nbMarty=0):
		self.marties[nbMarty].walk(1,'auto',0,-35, 1700)

	def go_back_slight(self, nbMarty=0):
		self.marties[nbMarty].walk(1,'auto',0,-34, 1700)

	def turn_left(self, nbMarty=0):
		self.marties[nbMarty].sidestep("left")

	def turn_right(self, nbMarty=0):
		self.marties[nbMarty].sidestep("right")

	def go_forw_left(self, nbMarty=0):
		for i in range(4):
			self.marties[nbMarty].walk(1, 'auto', 16, 1, 1000)
		self.stand_straight()

	def go_forward_right(self, nbMarty=0):
		for i in range(4):
			self.marties[nbMarty].walk(1, 'auto', -16, 1, 1000)
		self.stand_straight()

	def stand_straight(self, nbMarty=0):
		if (self.marties[nbMarty].get_joint_position('left knee') or self.marties[nbMarty].get_joint_position('right knee')):
			self.marties[nbMarty].walk(1, 'auto', 0, 8, 1700)
		self.marties[nbMarty].stand_straight(750)

	def stand_straight_forced(self, nbMarty=0):
		self.marties[nbMarty].walk(1, 'auto', 0, 8, 1700)
		self.marties[nbMarty].stand_straight(750)

	def dance(self, nbMarty=0):
		self.marties[nbMarty].dance()

	def celebrate(self, nbMarty=0):
		self.marties[nbMarty].celebrate()

	def wave_left(self, nbMarty=0):
		self.marties[nbMarty].wave("left")

	def wave_right(self, nbMarty=0):
		self.marties[nbMarty].wave("right")

	def hello(self, nbMarty=0):
		self.marties[nbMarty].hello()

	def shoot_right(self, nbMarty=0):
		self.marties[nbMarty].kick("right")

	def shoot_left(self, nbMarty=0):
		self.marties[nbMarty].kick("left")

	def hi(self, nbMarty=0):
		self.marties[nbMarty].stand_straight(200, blocking=False)
		self.marties[nbMarty].eyes(pose_or_angle=-20, move_time=100, blocking=False)
		self.marties[nbMarty].arms(left_angle=0, right_angle=120, move_time=200)
		self.marties[nbMarty].arms(left_angle=0, right_angle=0, move_time=200, blocking=False)
		self.marties[nbMarty].eyes(pose_or_angle=0, move_time=100)

	def connect_marty(self,ip,nbMarty=0):
		try:
			self.marties[nbMarty] = realMarty("wifi", ip, blocking=False)
			self.marties_connected[nbMarty] = True
			self.marties[nbMarty].get_ready()
			return "success"
		except:
			self.marties[nbMarty] = None
			self.marties_connected[nbMarty] = False
			return "failed"

	def color_calibration(self, color:str, nbMarty=0):
		mean = 0
		for i in range(500):
			mean = mean + int(self.marties[0].get_color_sensor_hex('left'), 16)
		self.colors[color] = mean / 500

	def read_labyrinth(self, nbMarty=0):
		print(self.colors)
		self.readColor(0, 0, nbMarty)

		for n in range(5):
			self.go_forw()
			sleep(3)
		self.stand_straight_forced()
		self.readColor(0, 1, nbMarty)

		for n in range(5):
			self.go_forw()
			sleep(3)
		self.stand_straight_forced()
		self.readColor(0, 2, nbMarty)


		self.marties[nbMarty].sidestep('left', 7)
		self.stand_straight_forced()
		self.readColor(1, 2, nbMarty)

		for n in range(6):
			self.go_back_slight()
			sleep(3)
		self.stand_straight_forced()
		self.readColor(1, 1, nbMarty)

		for n in range(6):
			self.go_back_slight()
			sleep(3)
		self.stand_straight_forced()
		self.readColor(1, 0, nbMarty)

		self.marties[nbMarty].sidestep('left', 7)
		self.stand_straight_forced()
		self.readColor(2, 0, nbMarty)

		for n in range(5):
			self.go_forw()
			sleep(3)
		self.stand_straight_forced()
		self.readColor(2, 1, nbMarty)

		for n in range(5):
			self.go_forw()
			sleep(3)
		self.stand_straight_forced()
		self.readColor(2, 2, nbMarty)

		print(self.labyrinth)


	def readColor(self,i,j, nbMarty=0):
		mean = 0
		for k in range(500):
			color_sensor = int(self.marties[nbMarty].get_color_sensor_hex('left'), 16)
			mean += color_sensor
		color_sensor = mean / 500

		for color in self.colors:
			print(color + " : " + str(color_sensor - self.colors[color]))
			if abs(color_sensor - self.colors[color]) < 300000:
				print(color)
				self.labyrinth[nbMarty][i][j] = color
		print("__________________")

