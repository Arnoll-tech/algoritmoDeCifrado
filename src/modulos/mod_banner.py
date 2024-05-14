import pyfiglet
from colorama import init, Fore

def banner():
    init()
    nombre = "CryptiVerse"
    estilo = "slant"
    color = Fore.GREEN

    bann = pyfiglet.figlet_format(nombre,font=estilo)
    bann_color = color + bann + Fore.RESET
    print(bann_color)
if __name__=="__banner__":
    banner()