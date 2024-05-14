import pyfiglet
from colorama import init, Fore

def banner():
    init()
    nombre = "CryptiVerse"
    estilo = "slant"
    color = Fore.GREEN

    bann = pyfiglet.figlet_format(nombre,font=estilo)
    bann_color = color + bann + Fore.RESET
    print("*" * 65)
    print(bann_color)
    print("*" * 65)
if __name__=="__banner__":
    banner()