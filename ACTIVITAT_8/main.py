from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola, mon"}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
def read_items():
    return {"items": ["item1", "item2", "item3"]}
