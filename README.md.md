# Aplicación de Restaurante - Taller Semana 14

## Descripción del Proyecto
Sistema de escritorio desarrollado en Python utilizando la librería Tkinter y almacenamiento local mediante archivos JSON. El proyecto implementa una arquitectura modular organizada en capas para separar la lógica de negocio, el manejo de datos y la interfaz de usuario.

## Estructura del Proyecto
- **datos/**: Contiene los archivos JSON (`productos.json`, `usuarios.json`) para la persistencia de la información.
- **modelos/**: Clases principales del dominio del negocio (Producto, Usuario).
- **servicios/**: Lógica de conexión y gestión de archivos.
- **ui/**: Vistas modulares de la interfaz gráfica (`login_view.py`, `main_view.py`).
- **main.py**: Archivo principal que inicializa el sistema y el flujo de autenticación.