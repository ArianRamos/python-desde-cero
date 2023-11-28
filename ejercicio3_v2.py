  GNU nano 6.2                                              ejercicio3_v1.py                                                        
#!/usr/bin/python3
#Algoritmo que pida números hasta que se introduzca un cero. 
#Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
cont = 0
while True:
	num=int(input("Numero (0 para salir:)"))
        suma = suma + num
	if num !=0
       		 cont = cont + 1
        if num == 0:
		break
# Si cont=0 no puedo realizar la division
if cont != 0:
        media = suma / cont
else:
        media = 0
print("Suma:",suma)
print("Media:",media)
