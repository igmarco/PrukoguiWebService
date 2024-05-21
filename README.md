# Prukogui Web Service
`@app.post("/PremiosPrukogui/{id}")` es el servicio importante, de momento.

## Proceso de desarrollo
1. `kill_all_threads()` no está matando los hilos de música.
2. Todavía hay archivos ("2.DC3-Menu.mp3", sin ir más lejos) que dan errores rarillos:
```
Error 259 for command:
        play "app\resources\2.DC3-Menu.mp3" wait
    El controlador no puede reconocer el parámetro especificado.
Exception in thread Thread-1 (play_audio):
Traceback (most recent call last):
  File "...\Python\Python310\lib\threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "...\Python\Python310\lib\threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\ignac\PycharmProjects\PrukoguiWebService\app\main.py", line 65, in play_audio
    playsound(song_file)
  File "...\PycharmProjects\PrukoguiWebService\venv\lib\site-packages\playsound.py", line 73, in _playsoundWin
    winCommand(u'play {}{}'.format(sound, ' wait' if block else ''))
  File "...\PycharmProjects\PrukoguiWebService\venv\lib\site-packages\playsound.py", line 64, in winCommand
    raise PlaysoundException(exceptionMessage)
playsound.PlaysoundException: 
    Error 259 for command:
        play "app\resources\2.DC3-Menu.mp3" wait
    El controlador no puede reconocer el parámetro especificado.

```