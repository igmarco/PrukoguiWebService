from typing import Union
from fastapi import FastAPI
import uvicorn

import os
import threading
import pygame

# Inicializar pygame mixer
pygame.mixer.init()

# Inicializar FastAPI
app = FastAPI()

# Cargar el servicio en un servidor ASGI Uvicorn
if __name__ == "__main__":
    print("http://localhost:10001/docs")
    uvicorn.run("main:app", port=10001, log_level="info", host="0.0.0.0")


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


@app.get("/roman/{mitad_refran}")
def read_item(mitad_refran: Union[str, None] = "Pájaro en mano"):
    return {"Refrán creativo": mitad_refran + ", patada en los c*jones"}


@app.post("/PremiosPrukogui/{id}")
def read_item(id: int):
    try:
        music_directory = 'app\\resources'
        play_song_by_id(id, music_directory)
        resultado = "Puesto"
    except Exception as e:
        resultado = "Error: " + str(e)
    return {"Audio " + str(id): resultado}

# Método que para la canción anterior y reproduce una canción en base a su ID
def play_song_by_id(song_id, music_dir):
    # Obtengo el nombre del archivo
    song_file = get_song_filename_by_id(song_id, music_dir)
    # Reproduzco la canción con el nombre
    if song_file:
        print(f"Reproduciendo: {song_file}")
        # Mato el resto de hilos de música
        stop_audio()
        # Creo un nuevo hilo para la reproducción del audio
        play_audio(song_file)
    else:
        raise Exception(f"No se encontró ninguna canción con el ID {song_id}")

# Método que obtiene el nombre de una canción en base a su ID
def get_song_filename_by_id(song_id, music_dir):
    # Listo todos los archivos en el directorio de música
    files = os.listdir(music_dir)
    # Busco el archivo que comienza con el ID dado
    for file in files:
        if file.startswith(f"{song_id}."):
            return os.path.join(music_dir, file)
    return None

# Método que reproduce una canción en base a su nombre de archivo
def play_audio(song_file):
    # Cargo la canción
    pygame.mixer.music.load(song_file)
    # Reproduzco la canción cargada
    pygame.mixer.music.play()

# Método que para la canción anterior
def stop_audio():
    pygame.mixer.music.stop()
