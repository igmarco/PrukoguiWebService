# Prukogui Web Service

Servicio Web de Prukogui que genera una API REST con los siguientes servicios:
- `@app.get("/roman/{mitad_refran}")`
- `@app.post("/PremiosPrukogui/{id}")`

---

## Requerimientos
1. *fastapi* v0.111.0 - Construye el Servicio con una librería sencilla.
2. *uvicorn* v0.29.0 - Despliega el Servicio sobre un servidor ASGI.
3. *pygame* v2.5.2 - Permite reproducir música.

## Funciones definidas
- `def play_song_by_id(song_id, music_dir)`
- `def get_song_filename_by_id(song_id, music_dir)`
- `def play_audio(song_file)`
- `def stop_audio()`