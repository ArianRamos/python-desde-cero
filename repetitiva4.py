#!/usr/bin/python3
secreto = "asdasd"
while True:
	clave = input("Dime la clave:")
	if clave != secreto:
		print("Clave incorrecta!!!")
	if clave == secreto:
		break;
print("Bienvenido")
print("Programa terminado")
