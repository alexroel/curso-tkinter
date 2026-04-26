# 🧛 Gastos Vampiro — Rastreador de Suscripciones

Aplicación elegante para rastrear esas suscripciones mensuales que chupan tu dinero sin que te des cuenta.

## Funcionalidades

- ➕ Agregar suscripciones con nombre y costo
- 📋 Visualizar todas las suscripciones en una tabla
- 🗑 Eliminar suscripciones
- 💾 Persistencia de datos en archivo JSON
- 📄 Exportar reporte a PDF
- ✅ Validación de entrada de datos
- 💡 Estimación de gasto anual

## Estructura del Proyecto

```
gastos_vampiros/
│
├── main.py                  # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Este archivo
│
├── data/                    # Capa de Persistencia de Datos
│   └── gastos.json          # Se genera dinámicamente al agregar suscripciones
│
├── logic/                   # Capa de Lógica de Negocio
│   ├── __init__.py
│   └── gestor_gastos.py     # Funciones para leer, escribir y procesar el JSON
│
├── gui/                     # Capa de Presentación (Interfaz Gráfica)
│   ├── __init__.py
│   ├── app.py               # Ventana principal — orquesta los componentes
│   ├── estilos.py           # Configuración de estilos ttk
│   └── components/          # Componentes modulares (cada sección de la UI)
│       ├── __init__.py
│       ├── header.py        # Encabezado con título
│       ├── formulario.py    # Formulario para agregar suscripciones
│       ├── resumen.py       # Badge del total mensual
│       ├── tabla.py         # Tabla de suscripciones (Treeview)
│       └── footer.py        # Botones de acción e info anual
│
└── assets/                  # Recursos estáticos
    ├── __init__.py
    └── styles.py            # Paleta de colores
```

## Cómo Ejecutar

```bash
cd gastos_vampiros
python main.py
```

## Dependencias

- **Python 3.8+**
- **tkinter** (incluido con Python)
- **fpdf2** (opcional, para exportar a PDF)

```bash
pip install -r requirements.txt
```
