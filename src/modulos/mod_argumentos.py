import argparse

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