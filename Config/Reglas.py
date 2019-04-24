class Reglas():
	def __init__(self):
		self.crear_reglas()
		
	def crear_reglas(self):
		self.regla = [ 
			["b","b","bb",1,1],
			["a","b","ba",1,1],
			["b","a","ab",1,1],
			["a","a","aa",1,1],
			["b","#","#b",1,1],
			["a","#","#a",1,1],
			["c","#","#",1,2],
			["c","b","b",1,2],
			["c","a","a",1,2],
			["b","b","",2,2],
			["a","a","",2,2],
			["","#","#",2,3]]

	def get(self):
		return self.regla
