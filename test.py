from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


#put can use below curl command to check
#curl -X PUT "http://127.0.0.1:8000/items/2" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"test\",\"price\":10,\"is_offer\":true}"
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}