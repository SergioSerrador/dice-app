# Practica: Flask Dice Roller

Esta actividad replica la dinamica de "Flask Cats" pero aplicada a un dado virtual. El objetivo es practicar Flask, trabajo con variables de entorno y dockerizacion basica.

## Objetivo

- Mostrar una pagina web con el resultado de tirar un dado.
- Permitir configurar el numero de caras mediante la variable de entorno `DICE_SIDES` (por defecto 6).
- Ejecutar la app dentro de Docker escuchando en el puerto 5000 y publicandolo en 8888.

## Material incluido

- `app.py` con la estructura Flask y TODOs listos para completar.
- `templates/index.html` con el template para la vista principal.
- `requirements.txt` con la dependencia necesaria.

## Tareas

1. **Completar la app**  
   - Implementa `get_sides()` leyendo `DICE_SIDES` y validando que sea un entero >= 2 (usa 6 como fallback).  
   - En la vista `/` genera la tirada con `random.randint(1, sides)`.  
   - Mantener el endpoint `/health` tal como esta.

2. **Crear el Dockerfile**  
   - Imagen base: `python:3.14.0-alpine3.22` (o `3.13` si la 3.14 no esta disponible en tu equipo).  
   - Copia `requirements.txt`, instala dependencias y luego copia el resto del codigo.  
   - Expone el puerto `5000`.  
   - Arranca con `CMD ["python", "app.py"]`.

3. **Construir la imagen**

   ```bash
   docker build -t dice_app .
   ```

4. **Ejecutar el contenedor**

   ```8888:5000  puerto
   ```

5. **Probar la variable de entorno**

   ```bash
   -e DICE_SIDES=20 
   ```

   Comprueba en `http://localhost:8888` que la pagina indica "Dado de 20 caras" y que las tiradas van de 1 a 20.

## Entrega

- Carpeta con `app.py`, `templates/index.html`, `requirements.txt`, `Dockerfile`.
- **README.md** con:
  - Comandos de build y ejecucion (con y sin `DICE_SIDES`).
  - Captura de pantalla de `http://localhost:8888`.
  - Breve explicacion (2-3 lineas) de que cambia al usar `-e DICE_SIDES=...`.

## Rubrica (10 pt)

- **App funcional** (4 pt): `/` muestra la tirada; `/health` responde ok; lectura correcta de `DICE_SIDES` (valor por defecto + validacion).
- **Dockerizacion** (4 pt): build sin errores; puerto 5000 expuesto; contenedor operativo al publicar `8888:5000`.
- **Documentacion** (2 pt): README con comandos y captura.
