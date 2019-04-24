import sys
from Config import Reglas as r

class Automata():
	def __init__(self,pila,palabra):
		self.pila = pila
		self.palabra = self.insertar_palabra(palabra)
		self.estado = 1
		self.Transiciones = r.Reglas()
	
	def insertar_palabra(self,palabra):
		lista = []
		for x in palabra:
			lista.append(x)
		return lista

	def funcion(self):
		for y in self.palabra:
			Bandera = False
			for x in self.Transiciones.get():
				if (x[0]==y and x[1]=="#" and x[3]==self.estado):
					Bandera = True
					#desapilar
					#apilar
					self.estado = x[4]
					break
			
			if (Bandera == False):
				print("Frase invalida")

palabra = Automata("pila","c")
print(palabra.funcion())