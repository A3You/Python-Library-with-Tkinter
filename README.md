```markdown
# PyLib - Sistema de Gestión Bibliotecaria 📚

Aplicación para administrar libros, autores y editoriales con interfaz gráfica (Tkinter) y arquitectura MVC.

## 🗃️ Estructura de la Base de Datos
```sql
-- Estructura principal (ejemplo)
CREATE TABLE IF NOT EXISTS autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE
);

CREATE TABLE IF NOT EXISTS editoriales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    precio DECIMAL(10,2),
    id_editorial INT,
    fecha_publicacion DATE,
    FOREIGN KEY (id_editorial) REFERENCES editoriales(id)
);

CREATE TABLE IF NOT EXISTS libros_autores (
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES libros(id),
    FOREIGN KEY (id_autor) REFERENCES autores(id)
);
```

## 🐍 Arquitectura MVC - Flujo y Componentes

### **Modelos** (`/models`)
- `BaseModel.py`: Clase base con métodos CRUD genéricos y manejo de conexiones
- `Libro.py`: Hereda de BaseModel. Maneja:
  - Operaciones con libros y sus relaciones N-M con autores
  - Validaciones de editoriales y autores
  - Consultas complejas con JOINs y subconsultas

### **Vistas** (`/libros`, `/autores`)
- `*View.py`: Componentes Tkinter para mostrar listados y formularios
- `FormView.py`: Formulario reutilizable con:
  - DateEntry para fechas
  - Combobox para relaciones
  - Listbox multiselección

### **Controladores** (`/controllers`)
- `LibrosController.py`: 
  - Coordina vistas de libros con el modelo
  - Gestiona eventos y transformación de datos
  - Maneja actualización de listados
- `AutoresController.py`:
  - Lógica similar para autores
  - Integración con selector de libros

## 🛠️ Instalación
1. Requisitos:
   ```bash
   pip install mysql-connector-python tkcalendar
   ```

2. Configuración DB:
   - Crear archivo `config/config.ini` con:
     ```ini
     [database]
     host = localhost
     user = root
     password = 
     database = biblioteca
     use_pure = True
     ```

3. Iniciar aplicación:
   ```bash
   python main.py
   ```

## 🗂️ Estructura del Proyecto
```
📦 PyLib
├── 📂 config
│   ├── config.ini            # Configuración de conexión
│   └── config_manager.py     # Gestor de configuración
├── 📂 app
│   ├── 📂 autores
│   │   ├── AutoresView.py    # Vista listado autores
│   │   ├── FormView.py       # Formulario específico autores
│   │   └── AutoresController.py # Lógica autores
│   ├── 📂 libros
│   │   ├── LibrosView.py     # Vista listado libros
│   │   ├── FormView.py       # Formulario específico libros
│   │   └── LibrosController.py # Lógica libros
│   └── 📂 models
│       ├── BaseModel.py      # Clase abstracta para modelos
│       └── Libro.py         # Modelo específico libros
├── BaseView.py               # Vista principal contenedora
└── main.py                   # Punto de entrada
```

## 🔄 Flujo MVC
1. **Interacción Usuario**:
   - Ej: Click en "Crear Libro"
   - La Vista (`LibrosView`) notifica al Controlador

2. **Controlador** (`LibrosController`):
   - Valida permisos
   - Instancia el FormView con los datos necesarios
   - Recoge los datos del formulario

3. **Modelo** (`Libro.py`):
   - Ejecuta consultas SQL
   - Maneja transacciones
   - Aplica reglas de negocio:
     ```python
     def crear_libro(...):
         # 1. Valida existencia editorial
         # 2. Verifica autores válidos
         # 3. Inserta en transacción
     ```

4. **Actualización Vista**:
   - El Controlador solicita nuevo listado
   - La Vista renderiza los datos actualizados

## ✅ Mejoras Implementadas
1. **Relaciones N-M**:
   - Selector gráfico de autores para libros
   - Actualización en cascada de relaciones

2. **Validaciones**:
   - Campos obligatorios en formularios
   - Formato de fechas
   - Existencia de registros relacionados

3. **Patrones**:
   - Conexiones DB por operación
   - Reutilización de componentes UI
   - Separación clara MVC

## 📌 Notas Importantes
- Cada módulo (libros/autores) tiene su propio:
  - FormView especializado
  - Controlador dedicado
  - Consultas específicas
- El modelo `Libro.py` gestiona múltiples tablas por requerimientos del CRUD
- La configuración se centraliza en `ConfigManager`

``` 