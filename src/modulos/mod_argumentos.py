import argparse


error = "Error: comando no encontrado"

#La funcion muestra el procesos de cifrado a medida que se ejecuta el script con el parametro verbose
def verbose():
    string = argparse.ArgumentParser(description="cryptiverse [-v][--v][-verbose][--verbose]")
    string.add_argument("-v","--v","-verbose","--verbose", type=str, help="Muestra en pantalla el cifrado a medida que se le pasan los parametros")
    argumentos = string.parse_args()

    if argumentos.verbose:
        print("ok")
    else:
        print("error")

if __name__ == "__verbose__":
    verbose()

#La funcion despliega un menu de ayuda del script
def help():
    string = argparse.ArgumentParser(description="cryptiverse [-h][--h][-help][--help]")
    string.add_argument("-h", "--h", "-help", "--help", type=str, help="Muestra los comandos que se pueden usar para el cifrado")
    argumentos = string.parse_args()

    if argumentos.help:
        verbose()
    else:
        print(error)
        
if __name__=="__help__":
    help()
