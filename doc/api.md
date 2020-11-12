



###retrieve fw info with vendor & sn info
#code
@app.get("/api/v1/resources/fws")
def read_item(vendor: str = None, sn: str = None):
    return {"dev": "FW", "vendor": vendor, "sn": sn}

#Curl
curl -X GET "http://47.95.4.161:31070/api/v1/resources/fws?vendor=h3c&sn=123abc" -H  "accept: application/json"

#request url
http://47.95.4.161:31070/api/v1/resources/fws?vendor=h3c&sn=123abc

#response code
200

#response body
{
  "dev": "FW",
  "vendor": "h3c",
  "sn": "123abc"
}

#response header
 content-length: 41 
 content-type: application/json 
 date: Wed11 Nov 2020 07:58:55 GMT 
 server: uvicorn 
