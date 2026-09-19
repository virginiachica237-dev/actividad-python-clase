import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView

def main():
    # Instanciamos el servicio central (maneja los JSON de datos)
    servicio = RestauranteServicio()
    
    # Creamos la ventana raíz de Tkinter pero la mantenemos oculta
    root = tk.Tk()
    root.withdraw()
    
    # Iniciamos el flujo mostrando la vista de Login
    app = LoginView(root, servicio)
    
    # Mantenemos la aplicación corriendo
    root.mainloop()

if __name__ == "__main__":
    main()