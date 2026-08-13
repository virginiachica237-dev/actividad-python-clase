# Restaurante App
**Estudiante:** Elvira Virginia Chica Angulo

## 📖 Descripción breve
Este sistema permite administrar usuarios y productos de un restaurante mediante un menú interactivo en consola. Se implementa programación orientada a objetos y estructuras de datos en Python para gestionar registros y operaciones básicas como registrar, buscar, actualizar, eliminar y listar.

## 📂 Estructura del proyecto
- **modelos/**
  - `usuario.py`: clase Usuario (identificación, nombre, correo).
  - `producto.py`: clase Producto (código, nombre, precio).
- **servicios/**
  - `restaurante.py`: clase Restaurante (administra colecciones y operaciones).
- **main.py**: menú principal con interacción por consola.
- **README.md**: documentación del proyecto.

## 🧩 Responsabilidad de los componentes
- **Usuario**: representa clientes o personas con identificación, nombre y correo.
- **Producto**: representa los productos del restaurante con código, nombre y precio.
- **Restaurante**: administra las colecciones de usuarios y productos, con operaciones de registrar, buscar, actualizar, eliminar y listar.
- **main.py**: gestiona la interacción con el usuario mediante un menú.

## 🔑 Uso de estructuras de datos
- **List**: colecciones dinámicas de usuarios y productos, permiten agregar, eliminar y recorrer objetos.  
- **Tuple**: menú principal, ya que sus opciones son estables y no cambian.  
- **Dict**: relación opción → función en el menú, facilita la ejecución según la elección del usuario.  
- **Set**: categorías únicas de productos o identificaciones, evita duplicados.

## ▶️ Instrucciones de ejecución
1. Abrir la terminal en la carpeta del proyecto.  
2. Ejecutar el comando:  
   ```bash
   python main.py
