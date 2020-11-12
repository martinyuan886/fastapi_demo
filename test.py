from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}

#下面函参中
# -item_id为client在url中输入的
# -q为在url中?后面带的如/items/1?q=haha，此处使用python类型声明声明为字符串，None代表不是必填
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


#retrieve fw info with vendor & sn info
#linux cmd commmand:
#curl -v http://auto.cmri.com:31070/api/v1/resources/fws?vendor=h3c\&sn=123ab    #在linux下此处&得用\转义一下
@app.get("/api/v1/resources/fws")
def read_item(vendor: str = None, sn: str = None):
    return {"dev": "FW", "vendor": vendor, "sn": sn}



class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


#put can use below curl command to check
#curl -X PUT "http://127.0.0.1:8000/items/2" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"test\",\"price\":10,\"is_offer\":true}"
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



class Item_patch(BaseModel):
    name: str
    is_ok: bool



#patch can use below curl command to check
#curl -X PATCH "http://47.95.4.161:31070/items/1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"string\",\"is_ok\":true}"
@app.patch("/items/{item_id}")
def update_item(item_id: int, item: Item_patch):
    return {"item_id": item_id, "item_name": item.name, "ok_or_not": item.is_ok}


#add for test auto-reload
