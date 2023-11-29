#!/usr/bin/python3
#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Dni():

	def __init__(self,numero):
		self.numero=numero

	def __calcular_letra(self):
		letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
		return letras[int(self.numero)%23]

	@property
	def numero(self):
		return self._letra

	@numero.setter
	def numero(self,numero):
		if len(numero)==8 and numero.isdigit():
			self._numero = numero
			self._letra = self._calcular_letra()
		else:
			self._numero=0
			self._letra = ""
			print("DNI Incorrecto")

	def mostrar(self):
		return self.numero+self.letra
