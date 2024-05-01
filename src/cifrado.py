import modulos 

texto_inicial = ""
indice_de_rotacion = 0
palabra_clave = ""
sum_clave_y_cesar = 0
texto_en_cesar = ""
texto_en_vigenere = ""
texto_en_hex = ""

def integracionCesar(texto_inicial,indice_de_rotacion,texto_en_cesar):

    if (indice_de_rotacion >= 1 & indice_de_rotacion <= 26):
        