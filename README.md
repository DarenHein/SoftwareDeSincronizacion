# Software de Sincronización de Música

Herramienta desarrollada en Python para automatizar la sincronización y organización de bibliotecas musicales entre un equipo local, memorias SD y reproductores de audio portátiles (DAP).

## Requisitos Previos

- Sistema Operativo: macOS
- Python instalado en el equipo (versión 3.14 o superior)

---

## Instalación y Configuración

Abre tu terminal, ubícate en la carpeta raíz del proyecto y ejecuta los siguientes comandos en orden:

1. **Crear el entorno virtual:**
   ```bash
   python3 -m venv venv
   ```
2. **Activar el entorno virtual:**
   ```bash
   source venv/bin/activate
   ```
3. **Instalar las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

### Actualizar dependencias (por si luego lo olvido)
```bash
pip freeze > requirements.txt
```

---

## Entorno de Pruebas (Sandbox)

Para realizar pruebas locales seguras sin afectar la música real ni requerir hardware conectado, puedes inicializar la estructura de directorios de prueba ejecutando este comando en tu terminal:

```bash
mkdir -p test_environment/pc_mock test_environment/sd_mock test_environment/host_mock dataBase && touch test_environment/pc_mock/.gitkeep test_environment/sd_mock/.gitkeep test_environment/host_mock/.gitkeep dataBase/database_test.txt
```

---

## Configuración de Rutas (`config.py`)

Toda la gestión de rutas y entornos se centraliza en el archivo `config.py`. En él puedes alternar entre el entorno de pruebas local y el entorno de producción real mediante una bandera:

```python
# Cambia a False para usar las rutas reales y el hardware
ES_MODO_PRUEBA = True
```

Las rutas gestionadas son:
1. **pcPath:** Ruta de la carpeta local donde se encuentra tu música en la computadora.
2. **sdPath:** Ruta de la tarjeta SD externa.
3. **hostPath:** Ruta del dispositivo reproductor de música (DAP).
4. **dbPath / nameDirectoryDB:** Configuración de la base de datos de registros de sincronización.