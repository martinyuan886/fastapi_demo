from typing import Optional
from typing import List, Dict, Set, Tuple

from enum import Enum


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()




@app.get("/")
def read_root():
    return "Hi, this is auto api simulator"

##下面函参中
## -item_id为client在url中输入的
## -q为在url中?后面带的如/items/1?q=haha，此处使用python类型声明声明为字符串，None代表不是必填
#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: str = None):
#    return {"item_id": item_id, "q": q}
#
#
##retrieve fw info with vendor & sn info
##linux cmd commmand:
##curl -v http://auto.cmri.com:31070/api/v1/resources/fws?vendor=h3c\&sn=123ab    #在linux下此处&得用\转义一下
#@app.get("/api/v1/resources/fws")
#def read_item(vendor: str = None, sn: str = None):
#    return {"dev": "FW", "vendor": vendor, "sn": sn}
#
#
#
#class Item(BaseModel):
#    name: str
#    price: float
#    is_offer: bool = None
#
#
##put can use below curl command to check
##curl -X PUT "http://127.0.0.1:8000/items/2" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"test\",\"price\":10,\"is_offer\":true}"
#@app.put("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, "item_id": item_id}
#
#
#
#class Item_patch(BaseModel):
#    name: str
#    is_ok: bool
#
#
#
##patch can use below curl command to check
##curl -X PATCH "http://47.95.4.161:31070/items/1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"string\",\"is_ok\":true}"
#@app.patch("/items/{item_id}")
#def update_item(item_id: int, item: Item_patch):
#    return {"item_id": item_id, "item_name": item.name, "ok_or_not": item.is_ok}
#    #print("no return")


class Result(str, Enum):
    success = "success"
    failed = "failed"


class Vendor(str, Enum):
    h3c = "H3C"
    zte = "ZTE"
    hw = "HW"
    other = "Other"

class Device_type(str, Enum):
    sw = "SW"
    router = "Router"
    firewall = "FW"
    other = "Other"


#目前class中字段不能少/或写错，但是可以有多余字段，不报错，但是内部应该是忽略了，因为返回时候不带多余的字段
class Dev_info(BaseModel):
    sn: str
    dhcp_ip: str
    vendor: Vendor
    device_type: Device_type


class Item_get_sn_result(BaseModel):
    #result: str                             
    result: Result
    #failure_info: Optional[str] = "N/A"    #request的body中可不带该字段，不带默认是"N/A"
    failure_info: str = "N/A"
    #dev_info: Dict[str, str]
    dev_info: Dev_info            #通过pydantic的嵌套实现嵌套字段的校验
    


###response
#200: (1)get sn success(sn found), dev_config_info returned   (2)get sn failed, return "got it"
#404：sn not found in db
#500: internal error, let sn == "internal_error" to simulate


sn_list = ["123", "456", "789"]       #simulate sn in db, if sn replied by agent isn't in this list, corresponding error info would be replied 

#post can use below curl command to check
#curl -X POST "http://auto.cmri.com:31070/api/v1/resources/net_devices/get_sn_result" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"result\":\"success\",\"failure_info\":\"N/A\",\"dev_info\":{\"sn\":\"123456\",\"dhcp_ip\":\"192.168.33.200\",\"vendor\":\"H3C\",\"dev_type\":\"FW\"}}"
@app.post("/api/v1/resources/net_devices/get_sn_result")
def update_get_sn_result(item: Item_get_sn_result):
    #return {"get_sn_result": item.result, "failure_info": item.failure_info, "dev_info": item.dev_info}
    #print("no return")
    get_sn_result = item.result
    #senario: agent not got
    if get_sn_result == "failed":
        failure_info_get_sn = item.failure_info
        print("agent failed to get sn, failure info is: {}".format(failure_info_get_sn))
        return {"detail": "Failed result got by AUTO"}
    elif get_sn_result == "success":
        sn_get = item.dev_info.sn
        db_response = retrieve_dev_info_by_sn_from_db(sn_get)   #fake db operation func, replace with real db operation soon
        return db_response
        
        
def retrieve_dev_info_by_sn_from_db(sn_get: str):
    if sn_get == "internal_error":
        try:
            print ("for simulate db operation error")
            raise Exception
        except:
            raise HTTPException(status_code=500, detail="internal error")
    elif sn_get in sn_list:
        return {"sn_match_result": "success", "dev_config_data":{"hostname": "NFV-SRV-1", "mng_ip": "10.10.10.1", "netmask": "24","gw": "10.10.10.254"}}  #user dict to simualte record in db table soon
    else:
        print("sn got was not found in db, please further check")
        #return {"sn_match_result": "failed", }
        raise HTTPException(status_code=404, detail="sn got was not found in db")
