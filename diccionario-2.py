#!/usr/bin/python3

#Escribe un programa que lea una cadena y devuelva un diccionario
#con la cantidad de apariciones de una cada caracter en la cadena

dict = {}
cadena = input("Dame una cadena:")
for caracter in cadena:
	if caracter in dict:
		dict[caracter]+=1
	else:
		dict[caracter]=1

for campo,valor in dict.items():
	print (campo,"->",valor)

