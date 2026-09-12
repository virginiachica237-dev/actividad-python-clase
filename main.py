import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# --- MODELOS Y DATOS AUTOMÁTICOS ---
class RestauranteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Restaurante App")
        self.geometry("500x450")
        self.resizable(False, False)

        # Datos por defecto integrados para evitar errores
        self.usuarios = {"admin": "123", "mesero": "456"}
        self.productos = [
            {"nombre": "Hamburguesa", "precio": 5.50, "stock": 20},
            {"nombre": "Papas Fritas", "precio": 2.50, "stock": 50},
            {"nombre": "Refresco", "precio": 1.50, "stock": 40}
        ]

        self.mostrar_login()

    def limpiar_ventana(self):
        for widget in self.winfo_children():
            widget.destroy()

    # --- PANTALLA DE LOGIN ---
    def mostrar_login(self):
        self.limpiar_ventana()
        
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="LOGIN - RESTAURANTE", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=30)

        tk.Label(frame, text="Usuario:", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.entry_usuario = tk.Entry(frame, font=("Arial", 11))
        self.entry_usuario.pack(pady=5)

        tk.Label(frame, text="Contraseña:", bg="#f0f0f0", font=("Arial", 11)).pack()
        self.entry_password = tk.Entry(frame, show="*", font=("Arial", 11))
        self.entry_password.pack(pady=5)

        tk.Button(frame, text="Ingresar", command=self.verificar_login, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=15).pack(pady=20)

    def verificar_login(self):
        user = self.entry_usuario.get()
        pwd = self.entry_password.get()

        if user in self.usuarios and self.usuarios[user] == pwd:
            messagebox.showinfo("Éxito", f"¡Bienvenido, {user}!")
            self.mostrar_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    # --- PANTALLA PRINCIPAL ---
    def mostrar_principal(self):
        self.limpiar_ventana()

        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="PANEL PRINCIPAL - RESTAURANTE", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Tabla de Productos
        tk.Label(frame, text="Productos Registrados:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(anchor="w", padx=20)
        
        self.tabla_productos = ttk.Treeview(frame, columns=("Nombre", "Precio", "Stock"), show="headings", height=5)
        self.tabla_productos.heading("Nombre", text="Nombre")
        self.tabla_productos.heading("Precio", text="Precio ($)")
        self.tabla_productos.heading("Stock", text="Stock")
        self.tabla_productos.pack(padx=20, pady=5, fill="x")

        for p in self.productos:
            self.tabla_productos.insert("", "end", values=(p["nombre"], f"{p['precio']:.2f}", p["stock"]))

        # Tabla de Usuarios
        tk.Label(frame, text="Usuarios del Sistema:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(anchor="w", padx=20, pady=(10, 0))
        
        self.tabla_usuarios = ttk.Treeview(frame, columns=("Usuario", "Password"), show="headings", height=3)
        self.tabla_usuarios.heading("Usuario", text="Usuario")
        self.tabla_usuarios.heading("Password", text="Contraseña")
        self.tabla_usuarios.pack(padx=20, pady=5, fill="x")

        for u in self.usuarios:
            self.tabla_usuarios.insert("", "end", values=(u, "****"))

        tk.Label(frame, text="[Funcionalidades futuras pendientes: Módulo de Ventas]", fg="gray", bg="#f0f0f0", font=("Arial", 9, "italic")).pack(pady=15)

if __name__ == "__main__":
    app = RestauranteApp()
    app.mainloop()