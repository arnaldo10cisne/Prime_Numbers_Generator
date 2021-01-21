import os
def clear():
	os.system("cls")
def l(): print("");
# Generador de números primos

print("GENERADOR DE NÚMEROS PRIMOS")
print("ARNALDO CISNEROS")
print("NOVIEMBRE DE 2020")

while True:
	l()
	cantidad_de_primos=int(input("¿Cuántos números primos te muestro?: "))
	numero_inicial=int(input("¿Desde qué número empiezo a buscar?: "))
	
	# **** CODIGO PARA BUSCAR NÚMEROS PRIMOS
	primos_encontrados=0
	numero_evaluado=numero_inicial
	if numero_evaluado==1:
		numero_evaluado=2	
	lista_de_divisores=[2]
	a=3
	while True:
		lista_de_divisores.append(a)
		a+=2
		if a>(numero_inicial/2):
			break;
	while primos_encontrados<cantidad_de_primos:

		if numero_evaluado%2==0 and numero_evaluado!=2:
			numero_evaluado+=1
			continue;

		primo=True

		# BUSQUEDA DE PRIMO CON POSIBLE CANDIDATO
		# Por definición, para encontrar un número primo, tenemos que dividir ese número entre todos los números menores a el, y si ninguna división da exacta, el número es primo
		# Además, para agilizar el programa, sólo debemos considerar la primera mitad de los números menores al evaluado. Por ejemplo, si estamos evaluando el número 100, sólo debemos dividirlo entre el 1 y el 50. No vale la pena dividirlo entre números mayores a 50, porque los factores primos de un número no pueden ser mayores, por definición, a la mitad de este. 
		divisor_maximo=numero_evaluado/2
		numero_de_divisiones=0
		
		for divisor_actual in lista_de_divisores:
			resto=numero_evaluado%divisor_actual
			numero_de_divisiones+=1
			if resto==0:
				if numero_evaluado==2:
					numero_evaluado+=1
				else:
					numero_evaluado+=2
				primo=False
				break;
			elif divisor_actual>divisor_maximo:
				break;

		if primo: # Entra en este condicional si se encuentra un número primo
			primos_encontrados+=1
			print(primos_encontrados,". Número primo encontrado: ",numero_evaluado, ", e hice ",numero_de_divisiones," divisiones")
			lista_de_divisores.append(numero_evaluado)
			if numero_evaluado<=2:
				numero_evaluado+=1
			else:
				numero_evaluado+=2

	# **************************************
	
	l()
	salir=input("¿Deseas hacer otra búsqueda? y/n: ")
	if salir=="n":
		break;
	elif salir=="y":
		clear()
		pass
	else:
		print("Respuesta no válida, finalizando el programa")
		input()
		break;
