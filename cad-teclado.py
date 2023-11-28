#!/usr/bin/python3
## Suponiendo que hemos introducido una cadena por teclado
#que represente una frase
## (palabras separadas por espacios), realiza un programa que 
#cuenta cuantas palabras tienes

cont = 0
posicion = 0
cad = input("Introduce una cadena:")
#Elimino los posible espacios que haya al principio y final de la cadena
cad = cad.strip()
# voy buscando los espacio
posicion = cad.find(" ",posicion)
while posicion != -1:
	cont = cont + 1
#No tengo en cuenta los posibles espacios que haya entre las palabras
	while cad[posicion + 1] == " ":
		posicion = posicion + 1
	posicion = cad.find(" ", posicion + 1)
print("La frase tiene",cont +1,"palabras.")

