# Restaurante App - Semana 11

Evolución del sistema de gestión para restaurantes enfocado en la relación entre objetos, control de stock y persistencia extendida en JSON.

## Estructura del Proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

## Mejoras de la Semana 11
- **Modelo Venta:** Creación de la entidad `Venta` para relacionar directamente al usuario, el producto y la cantidad adquirida.
- **Control de Stock:** Validación de existencias antes de concretar una venta y descuento automático del inventario sin permitir valores negativos.
- **Persistencia Completa:** Lectura y guardado automático en formato JSON para productos, usuarios y ventas utilizando `ArchivoServicio`.
- **Manejo de Excepciones:** Robustecimiento frente a archivos faltantes, corrupción de datos y restricciones de permisos.

## Instrucciones de Ejecución
Ejecute el archivo principal desde la terminal:
```bash
python main.py
