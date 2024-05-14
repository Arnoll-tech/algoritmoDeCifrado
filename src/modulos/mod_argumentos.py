import argparse

error = "Error: comando no encontrado"

#La funcion muestra el procesos de cifrado a medida que se ejecuta el script con el parametro verbose
def verbose(parametro_cifrado):
    string = argparse.ArgumentParser(description="crptiverse [-v][--v][-verbose][--verbose]")
    string.add_argument("-v", "--v", "-verbose", "--verbose", action="store_true", help="Muestra en pantalla el cifrado a medida que se le pasan los parametros")
    argumentos = string.parse_args()

    if argumentos.v:
        print(parametro_cifrado)

    if __name__ == "__verbose__":
        verbose(parametro_cifrado)

#La funcion despliega un menu de ayuda del script
def help():
    cadena = argparse.ArgumentParser(description="cryptiverse [-h][--h][-help][--help]")
    cadena.add_argument("-h", "--h", "-help", "--help", action="store_true", help="Muestra los comandos que se pueden usar para el cifrado")
    argument = cadena.parse_args()

    if argument.help:
        cadena.print_help()
        exit()
if __name__=="__help__":
    help()
