from app.model.marty import Marty

class ConnectionController():
	def __init__(self):
		self.marty = Marty()

	def connect(self,ip, nb_marty = 0):
		success = self.marty.connect_marty(ip,0)
		return success

	def cancel(self):
		##ferme la fenetre / reset le champs ip
		pass