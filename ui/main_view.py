import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class MainView:
    def __init__(self, parent, servicio):
        self.parent = parent
        self.servicio = servicio
        
        # Ventana Principal
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Menú Principal - Restaurante")
        self.ventana.geometry("650x500")
        self.ventana.config(bg="#f0f0f0")
        
        # Título
        tk.Label(self.ventana, text="Gestión de Productos", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
        
        # Frame del Formulario
        frame_form = tk.LabelFrame(self.ventana, text=" Formulario de Productos ", bg="#f0f0f0", font=("Arial", 10, "bold"))
        frame_form.pack(fill="x", padx=20, pady=10)
        
        # Campos
        tk.Label(frame_form, text="ID Producto:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.txt_id = tk.Entry(frame_form, width=25)
        self.txt_id.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Nombre:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.txt_nombre = tk.Entry(frame_form, width=25)
        self.txt_nombre.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Precio:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.txt_precio = tk.Entry(frame_form, width=25)
        self.txt_precio.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_form, text="Stock:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.txt_stock = tk.Entry(frame_form, width=25)
        self.txt_stock.grid(row=3, column=1, padx=10, pady=5)
        
        # Botones de acción
        frame_botones = tk.Frame(frame_form, bg="#f0f0f0")
        frame_botones.grid(row=4, column=0, columnspan=2, pady=10)
        
        tk.Button(frame_botones, text="Registrar", bg="#4CAF50", fg="white", width=10, command=self.registrar_producto).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Limpiar", bg="#ff9800", fg="white", width=10, command=self.limpiar_campos).pack(side="left", padx=5)
        
        # Tabla de Inventario
        frame_tabla = tk.LabelFrame(self.ventana, text=" Inventario de Productos ", bg="#f0f0f0", font=("Arial", 10, "bold"))
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.tabla = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Stock", text="Stock")
        
        self.tabla.column("ID", width=50)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Precio", width=100)
        self.tabla.column("Stock", width=100)
        
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Cargar datos iniciales en la tabla
        self.actualizar_tabla()

    def registrar_producto(self):
        id_prod = self.txt_id.get()
        nombre = self.txt_nombre.get()
        precio = self.txt_precio.get()
        stock = self.txt_stock.get()
        
        if not id_prod or not nombre or not precio or not stock:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
            
        nuevo_producto = {
            "nombre": nombre,
            "precio": float(precio),
            "stock": int(stock)
        }
        
        try:
            # Intentamos guardar usando el servicio si está disponible
            if hasattr(self.servicio, 'guardar_producto'):
                self.servicio.guardar_producto(nuevo_producto)
            else:
                # Guardado directo en productos.json por seguridad
                ruta = "datos/productos.json"
                os.makedirs("datos", exist_ok=True)
                if os.path.exists(ruta):
                    with open(ruta, "r", encoding="utf-8") as f:
                        datos = json.load(f)
                else:
                    datos = []
                datos.append(nuevo_producto)
                with open(ruta, "w", encoding="utf-8") as f:
                    json.dump(datos, f, indent=4, ensure_ascii=False)
                    
            messagebox.showinfo("Éxito", "Producto registrado correctamente")
            self.limpiar_campos()
            self.actualizar_tabla()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

    def limpiar_campos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_stock.delete(0, tk.END)

    def actualizar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
            
        ruta = "datos/productos.json"
        if os.path.exists(ruta):
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    for idx, prod in enumerate(datos):
                        self.tabla.insert("", "end", values=(idx+1, prod.get("nombre"), prod.get("precio"), prod.get("stock")))
            except:
                pass