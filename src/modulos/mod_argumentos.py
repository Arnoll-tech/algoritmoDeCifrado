import argparse
error = "Error: comando no encontrado"

#La funcion muestra el procesos de cifrado a medida que se ejecuta el script con el parametro verbose
def main(text):
    string = argparse.ArgumentParser(description="cifrado.py [-v][--verbose], [-h][--help]")
    string.add_argument("-v","--verbose", action="store_true", help="Muestra en pantalla el cifrado a medida que se le pasan los parametros")
    
    argumentos = string.parse_args()

    if argumentos.verbose:
        print(text)
        
    if __name__ == "__main__":
        main()
        