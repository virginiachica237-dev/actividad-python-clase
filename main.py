import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.main_view import MainView

def iniciar_aplicacion():
    # 1. Creamos la ventana principal de Tkinter
    root = tk.Tk()
    root.title("Restaurante App - Semana 16")
    root.geometry("850x500")
    
    # 2. Inicializa el servicio de datos
    servicio_restaurante = RestauranteServicio()
    
    # 3. Crea la vista pasando la ventana raíz (parent) y el servicio
    app = MainView(parent=root, servicio=servicio_restaurante)
    
    # 4. Iniciamos el bucle de la aplicación
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()


