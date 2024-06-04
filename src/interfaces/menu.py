import ttkbootstrap as ttb

def barra_herramientas(window: ttb):
    """Herramientas del menu principal"""
    #Logica de los widgets
    archivo_menu = ttb.Button(window, bootstyle="outline primary", text="Archivos")
    
    
    #Orden de disegno de los widgets
    archivo_menu.pack()

def panel_principal(window: ttb):
    """Panel del menu principal"""
    


