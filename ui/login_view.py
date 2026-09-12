import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, on_login_success, servicio):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.servicio = servicio

        self.configure(bg="#f0f0f0")

        # Título
        tk.Label(self, text="LOGIN - RESTAURANTE", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

        # Campo Usuario
        tk.Label(self, text="Usuario:", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.entry_usuario = tk.Entry(self, font=("Arial", 11))
        self.entry_usuario.pack(pady=5)

        # Campo Contraseña
        tk.Label(self, text="Contraseña:", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.entry_password = tk.Entry(self, show="*", font=("Arial", 11))
        self.entry_password.pack(pady=5)

        # Botón Ingresar
        tk.Button(self, text="Ingresar", command=self.verificar_credenciales, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=15).pack(pady=20)

    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if self.servicio.validar_login(usuario, password):
            messagebox.showinfo("Éxito", f"¡Bienvenido, {usuario}!")
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")