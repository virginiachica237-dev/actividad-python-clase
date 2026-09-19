import tkinter as tk
from tkinter import messagebox
from ui.main_view import MainView

class LoginView:
    def __init__(self, parent, servicio):
        self.parent = parent
        self.servicio = servicio
        
        # Ventana de Login
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Iniciar Sesión - Restaurante")
        self.ventana.geometry("350x250")
        self.ventana.config(bg="#f0f0f0")
        
        # Título
        tk.Label(self.ventana, text="Bienvenido al Sistema", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)
        
        # Usuario
        tk.Label(self.ventana, text="Usuario:", bg="#f0f0f0").pack(anchor="w", padx=40)
        self.txt_usuario = tk.Entry(self.ventana, width=30)
        self.txt_usuario.pack(pady=5, padx=40)
        
        # Contraseña
        tk.Label(self.ventana, text="Contraseña:", bg="#f0f0f0").pack(anchor="w", padx=40)
        self.txt_password = tk.Entry(self.ventana, width=30, show="*")
        self.txt_password.pack(pady=5, padx=40)
        
        # Botón de ingreso
        btn_login = tk.Button(self.ventana, text="Ingresar", bg="#4CAF50", fg="white", width=15, command=self.verificar_login)
        btn_login.pack(pady=15)
        
    def verificar_login(self):
        usuario = self.txt_usuario.get()
        password = self.txt_password.get()
        
        # Validación sencilla o consulta al servicio
        if usuario == "admin" and password == "1234":
            messagebox.showinfo("Éxito", "¡Bienvenido al sistema!")
            self.ventana.destroy()
            # Abrimos la ventana principal pasándole el servicio
            MainView(self.parent, self.servicio)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")