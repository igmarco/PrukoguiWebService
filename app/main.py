from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", port=10001, log_level="info")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/roman/{mitad_refran}")
def read_item(mitad_refran: Union[str, None] = "Pájaro en mano"):
    return {"Refrán creativo": mitad_refran + ", patada en los c*jones"}