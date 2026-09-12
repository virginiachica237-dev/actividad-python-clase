import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, parent, servicio):
        super().__init__(parent)
        self.servicio = servicio
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="PANEL PRINCIPAL - RESTAURANTE", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Sección de Productos Registrados
        tk.Label(self, text="Productos Registrados:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", padx=20)
        
        self.tabla_productos = ttk.Treeview(self, columns=("Nombre", "Precio", "Stock"), show="headings", height=5)
        self.tabla_productos.heading("Nombre", text="Nombre")
        self.tabla_productos.heading("Precio", text="Precio ($)")
        self.tabla_productos.heading("Stock", text="Stock")
        self.tabla_productos.pack(padx=20, pady=5, fill="x")

        # Sección de Usuarios Registrados
        tk.Label(self, text="Usuarios del Sistema:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="w", padx=20, pady=(10, 0))
        
        self.tabla_usuarios = ttk.Treeview(self, columns=("Usuario", "Password"), show="headings", height=4)
        self.tabla_usuarios.heading("Usuario", text="Usuario")
        self.tabla_usuarios.heading("Password", text="Contraseña (Oculta)")
        self.tabla_usuarios.pack(padx=20, pady=5, fill="x")

        # Funcionalidad futura (pendiente)
        tk.Label(self, text="[Funcionalidades futuras pendientes: Módulo de Ventas]", fg="gray", bg="#f0f0f0", font=("Arial", 10, "italic")).pack(pady=15)

        self.cargar_datos()

    def cargar_datos(self):
        # Cargar productos
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tabla_productos.insert("", "end", values=(p.nombre, f"{p.precio:.2f}", p.stock))

        # Cargar usuarios
        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tabla_usuarios.insert("", "end", values=(u.usuario, "****"))