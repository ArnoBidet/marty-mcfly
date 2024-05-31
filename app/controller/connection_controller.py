from app.model.marty import Marty

class ConnectionController():
	def __init__(self):
		self.marty = Marty()

	def connect(self,ip):
		success = self.marty.connect_marty(ip)
		return success

	def cancel(self):
		##ferme la fenetre / reset le champs ip
		pass