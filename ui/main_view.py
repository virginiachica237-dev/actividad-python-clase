import tkinter as tk
from tkinter import ttk, messagebox

class MainView:
    def __init__(self, parent, servicio):
        self.parent = parent
        self.servicio = servicio
        
        # Crear un contenedor principal dentro de la ventana raíz
        self.frame_principal = ttk.Frame(self.parent, padding=10)
        self.frame_principal.pack(fill="both", expand=True)
        
        # Configurar columnas elásticas
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.columnconfigure(1, weight=2)
        self.frame_principal.rowconfigure(0, weight=1)
        
        self._construir_ui()
        self._refrescar_tabla()

    def _construir_ui(self):
        # --- PANEL IZQUIERDO: Formulario ---
        frame_form = ttk.LabelFrame(self.frame_principal, text=" Registro / Edición de Usuarios ", padding=15)
        frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ttk.Label(frame_form, text="Nombre de Usuario:").pack(anchor="w", pady=(0, 2))
        self.txt_username = ttk.Entry(frame_form, font=("Segoe UI", 10))
        self.txt_username.pack(fill="x", pady=(0, 12))
        
        ttk.Label(frame_form, text="Rol asignado:").pack(anchor="w", pady=(0, 2))
        self.cb_rol = ttk.Combobox(frame_form, values=["Administrador", "Mesero", "Cajero", "Cocinero"], state="readonly")
        self.cb_rol.pack(fill="x", pady=(0, 12))
        
        self.var_activo = tk.BooleanVar(value=True)
        self.chk_activo = ttk.Checkbutton(frame_form, text="Usuario Habilitado / Activo", variable=self.var_activo)
        self.chk_activo.pack(anchor="w", pady=(0, 20))
        
        self.btn_guardar = ttk.Button(frame_form, text="💾 Guardar Usuario", command=self._procesar_guardado)
        self.btn_guardar.pack(fill="x", pady=3)
        
        self.btn_eliminar = ttk.Button(frame_form, text="❌ Eliminar Selección", command=self._procesar_eliminacion)
        self.btn_eliminar.pack(fill="x", pady=3)

        # --- PANEL DERECHO: Tabla Treeview ---
        frame_tabla = ttk.LabelFrame(self.frame_principal, text=" Personal del Restaurante ", padding=10)
        frame_tabla.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        frame_tabla.columnconfigure(0, weight=1)
        frame_tabla.rowconfigure(0, weight=1)

        columnas = ("user", "rol", "estado")
        self.tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        self.tree.heading("user", text="Nombre de Usuario")
        self.tree.heading("rol", text="Rol del Sistema")
        self.tree.heading("estado", text="Estado")
        
        self.tree.column("user", width=150, anchor="w")
        self.tree.column("rol", width=120, anchor="center")
        self.tree.column("estado", width=100, anchor="center")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # ==========================================
        #  IMPLEMENTACIÓN OBLIGATORIA DE EVENTOS
        # ==========================================
        self.tree.bind("<<TreeviewSelect>>", self._callback_tabla_seleccion)
        self.txt_username.bind("<Return>", self._callback_tecla_enter)
        self.cb_rol.bind("<<ComboboxSelected>>", self._callback_cambio_rol)
        self.parent.bind("<Escape>", lambda e: self._limpiar_formulario())

    def _refrescar_tabla(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        for u in self.servicio.obtener_usuarios():
            estado_txt = "Activo" if u.activo else "Inactivo"
            self.tree.insert("", "end", iid=u.username, values=(u.username, u.rol, estado_txt))

    # --- CALLBACKS (MANEJO DE EVENTOS) ---
    def _callback_tabla_seleccion(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return
        valores = self.tree.item(seleccion, "values")
        if valores:
            self.txt_username.configure(state="normal")
            self.txt_username.delete(0, tk.END)
            self.txt_username.insert(0, valores[0])
            self.txt_username.configure(state="disabled") # Bloquea ID en edición
            
            self.cb_rol.set(valores[1])
            self.var_activo.set(valores[2] == "Activo")

    def _callback_tecla_enter(self, event):
        self.cb_rol.focus_set()

    def _callback_cambio_rol(self, event):
        print(f"[Log Eventos] Se modificó el rol a: {self.cb_rol.get()}")

    def _limpiar_formulario(self):
        self.txt_username.configure(state="normal")
        self.txt_username.delete(0, tk.END)
        self.cb_rol.set("")
        self.var_activo.set(True)
        if self.tree.selection():
            self.tree.selection_remove(self.tree.selection())
        self.txt_username.focus_set()

    # --- LÓGICA DE PROCESAMIENTO ---
    def _procesar_guardado(self):
        username = self.txt_username.get().strip()
        rol = self.cb_rol.get()
        activo = self.var_activo.get()

        if not username or not rol:
            messagebox.showwarning("Atención", "Por favor completa todos los campos.")
            return

        if str(self.txt_username["state"]) == "disabled":
            exito, msg = self.servicio.actualizar_usuario(username, rol, activo)
        else:
            exito, msg = self.servicio.registrar_usuario(username, rol, activo)

        if exito:
            messagebox.showinfo("Éxito", msg)
            self._limpiar_formulario()
            self._refrescar_tabla()
        else:
            messagebox.showerror("Error", msg)

    def _procesar_eliminacion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un usuario de la lista.")
            return
        
        username = seleccion[0]
        if messagebox.askyesno("Confirmar", f"¿Deseas eliminar al usuario '{username}'?"):
            exito, msg = self.servicio.eliminar_usuario(username)
            if exito:
                messagebox.showinfo("Eliminado", msg)
                self._limpiar_formulario()
                self._refrescar_tabla()
            else:
                messagebox.showerror("Error", msg)
