#!/usr/bin/python3

#El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido
#desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha 
#nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

def EsBisiesto(year):
	return (year % 4 == 0 and not (year % 100 == 0 )) or year % 400 == 0

#LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#EsBisiesto: Recibe un año y nos dice si es bisiesto.
#Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

#Funcion diadelmes
def DiasDelMes(month,year):
	if month in [1,3,5,7,8,10,12]:
		return 31
	elif month in [4,6,8,11]:
		return 30
	elif month == 2:
		if EsBisiesto(year):
			return 29
		else:
			return 28



def Calcular_Dia_Juliano(day,month,year):
	diaj = 0
	for mes in range(1,month):
		diaj = diaj + DiasDelMes(mes,year)
	diaj = diaj + day
	return diaj
#Funcion leerfecha

def LeerFecha():
	day = int(input("Dia:"))
	month = int(input("Mes:"))
	year = int(input("Año:"))
	return day,month,year

d,m,a = LeerFecha()
print("Dia Juliano:",Calcular_Dia_Juliano(d,m,a))
