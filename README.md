# Software de Sincronizacion de Musica

Herramienta desarrollada en Python para automatizar la sincronizacion y organizacion de bibliotecas musicales entre un equipo local, memorias SD y reproductores de audio portatiles (DAP).

## Requisitos Previos

- Sistema Operativo: macOS
- Python instalado en el equipo (version 3.14 o superior)

## Instalacion y Configuracion

Abre tu terminal, ubicate en la carpeta raiz del proyecto y ejecuta los siguientes comandos en orden:

1. Crear el entorno virtual:
   python3 -m venv venv
2. Activar el entorno virtual:
   source venv/bin/activate
3. Instalar las dependencias necesarias:
   pip install -r requirements.txt

## Actualizar dependencias (por que luego lo olvido)
1. pip freeze > requirements.txt

## Configuracion de Rutas
Antes de la primera ejecucion, abre el archivo main.py y verifica o modifica las rutas segun tu entorno:
 
 1. pcPath: Ruta de la carpeta local donde se encuentra tu musica en la computadora.
 2. sdPath: Ruta del disco duro o memoria SD externa.
 3. hostPath: Ruta del dispositivo reproductor de musica (MP3 / DAP).

 