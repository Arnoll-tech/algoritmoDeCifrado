texto_inicial = ""
indice_de_rotacion = 0
sum_clave_y_cesar = 0
texto_en_cesar = ""
texto_en_vigenere = ""
texto_en_hex = ""
entrada_texto = "Ingresa texto a cifrar:"
entrada_indice = "Ingresa el numero de rotacion:"
entrada_clave = "Ingresa la palabra clave:"
alfabeto = "abcdefghijklmnopqrstuvwxyz"
espacios = " "

def integracionCesar():
    intentos_1 = 0
    contador = 4
    texto_inicial = input(entrada_texto + espacios)
    indice_de_rotacion = int(input(entrada_indice + espacios))
    while True:
        intentos_1 += 1
        if indice_de_rotacion >= 1 and indice_de_rotacion <= 26 and intentos_1 <= 3:
            rotacion = alfabeto[+indice_de_rotacion:] + alfabeto[:indice_de_rotacion]
            traduccion = str.maketrans(alfabeto + alfabeto.upper(), rotacion + rotacion.upper())
            texto_en_cesar = texto_inicial.translate(traduccion)
            print(texto_en_cesar) 
            break            
        elif intentos_1 <= 3:
             print(intentos_1)
             contador -= 1
             print("Te quedan " + str(contador) + " intentos")
             indice_de_rotacion = int(input("Ingresa un numero valido:" + espacios))
             
        else:
             print("error")
             break
integracionCesar()

##Diccionario carcacter-valor

def integracionVigenere():
     intentos = 0
     contador = 4
     palabra_clave = input(entrada_clave + espacios)
     while True:
        intentos += 1
        if (len(palabra_clave) >= 3 and len(palabra_clave) <= 23 and intentos <= 3):
                print("OK")
                break
        elif intentos <= 3:
              contador -= 1
              print("Te quedan " + str(contador) + " intentos")
              palabra_clave = input("Ingresa una palabra valida:" + espacios)
        else:
             print("error")
             break
     return print(intentos)

integracionVigenere()