#from modulos import mod_tablas

texto_inicial = ""
indice_de_rotacion = 0
palabra_clave = "Ingresa la palabra clave:"
sum_clave_y_cesar = 0
texto_en_cesar = ""
texto_en_vigenere = ""
texto_en_hex = ""
entrada_texto = "Ingresa texto a cifrar:"
entrada_indice = "Ingresa el numero de rotacion:"
alfabeto = "abcdefghijklmnopqrstuvwxyz"
espacios = " "

def integracionCesar():
    texto_inicial = input(entrada_texto + espacios)
    indice_de_rotacion = int(input(entrada_indice + espacios))
    if (indice_de_rotacion >= 1 and indice_de_rotacion <= 26 ):
            rotacion = alfabeto[+indice_de_rotacion:] + alfabeto[:indice_de_rotacion]
            traduccion = str.maketrans(alfabeto + alfabeto.upper(), rotacion + rotacion.upper())
            texto_en_cesar = texto_inicial.translate(traduccion)
            print(texto_en_cesar)   
    else:
        print("Ingresa un numero valido")
integracionCesar()


def integracionVigenere(texto_en_cesar):
     palabra_clave = str(input(palabra_clave + espacios))
     str.maketrans(texto_en_cesar + texto_en_cesar.punctuation)