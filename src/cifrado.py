#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from string import printable as alfabeto
from modulos import mod_argumentos, mod_banner

sum_clave_y_cesar = 0
texto_en_cesar = ""
texto_en_vigenere = ""
texto_en_hex = ""
entrada_texto = "Ingresa texto a cifrar: \n"
entrada_indice = "Ingresa el numero de rotacion: \n"
entrada_clave = "Ingresa la palabra clave: \n"
espacios = " "

mod_banner.banner()

#Funcion de integracion de texto a Cesar
def integracionCesar():
    intentos_1 = 0
    contador = 4
    texto_inicial = input(entrada_texto + espacios)
    indice_de_rotacion = int(input(entrada_indice + espacios))
    while True:
        intentos_1 += 1
        if indice_de_rotacion >= 1 and indice_de_rotacion <= 100 and intentos_1 <= 4:
            
            #Se rota el alfabeto hacia adelante
            rotacion = alfabeto[+indice_de_rotacion:] + alfabeto[:indice_de_rotacion]

            #se implementa traduccion a ASCII de minusculas y mayusculas
            traduccion = str.maketrans(alfabeto + alfabeto.upper(), rotacion + rotacion.upper())
            texto_en_cesar = texto_inicial.translate(traduccion)
            return mod_argumentos.main(texto_en_cesar)
            break            
        
        #si el indice de rotacion no esta en el rango, hay 3 intentos para escribir el correcto
        elif intentos_1 <= 4:
             contador -= 1
             print("Te quedan " + str(contador) + " intentos")
             indice_de_rotacion = int(input("Ingresa un numero valido:" + espacios))

        else:
             print("error")
             break
integracionCesar()

#Funcion de integracion de Cesar a Vigenere
def integracionVigenere(texto_en_cesar):
     intentos = 0
     contador = 4
     palabra_clave = input(entrada_clave + espacios)
     while True:
        intentos += 1

        #Verificando que la palabra clave no se ni muy corta ni muy larga
        if (len(palabra_clave) >= 3 and len(palabra_clave) <= 23 and intentos <= 3):
                break
        
        #Si la palabra clave no entra en el rango de longitud, hay 3 intentos para escribirla correctamente
        elif intentos <= 3:
              contador -= 1
              print("Te quedan " + str(contador) + " intentos")
              palabra_clave = input("Ingresa una palabra valida:" + espacios)
        else:
             print("error")
             break
     return print(intentos)

integracionVigenere(texto_en_cesar)

