##from modulos import mod_tablas

texto_inicial = ""
indice_de_rotacion = 0
palabra_clave = ""
sum_clave_y_cesar = 0
texto_en_cesar = ""
texto_en_vigenere = ""
texto_en_hex = ""
entrada_texto = "Ingresa texto a cifrar"
entrada_indice = "Ingresa el numero de rotacion"
alfabeto = "abcdefghijklmnopeqrstuvwxyz"

def integracionCesar():
    texto_inicial = input(print(entrada_texto))
    indice_de_rotacion = int(input(print(entrada_indice)))
    if (indice_de_rotacion >= 1 and indice_de_rotacion <= 26 ):
            rotacion = alfabeto[+indice_de_rotacion:] + alfabeto[:indice_de_rotacion]
            traduccion = str.maketrans(alfabeto + alfabeto.upper(), rotacion + rotacion.upper())
            texto_en_cesar = texto_inicial.translate(traduccion)
            print(texto_en_cesar)
    else:
        print("Ingresa un numero valido")
integracionCesar()