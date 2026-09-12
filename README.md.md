# Restaurante App - Semana 12

Aplicación de consola en Python desarrollada con Programación Orientada a Objetos para gestionar un restaurante, optimizada con estructuras de datos auxiliares (`dict` y `set`) para mejorar el rendimiento en búsquedas y consultas frecuentes.

## 🚀 Mejoras Implementadas
- **Índices en Memoria (`dict`)**: Se implementaron diccionarios auxiliares para localizar rápidamente productos por su código y usuarios por su identificación, evitando recorridos innecesarios.
- **Consulta Agrupada de Ventas**: Se estructuró un índice para consultar las ventas asociadas a un cliente de forma directa.
- **Validación con Conjuntos (`set`)**: Uso de `set` para verificar la existencia de códigos de productos de manera eficiente.
- **Reconstrucción Automática**: Al iniciar el programa, los índices se reconstruyen automáticamente a partir de la información recuperada de los archivos JSON.

## 📂 Estructura del Proyecto
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

## ⚙️ Instrucciones de Ejecución
1. Abre tu terminal o VS Code en la carpeta del proyecto.
2. Ejecuta el programa principal con:
   ```bash
   python main.py