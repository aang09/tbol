import requests, json
from fake_useragent import UserAgent

class Api : 
    
    
    def header(
            token
        ):
        
        with open("af09/header.json", 'r') as f:
            hd = json.load(f)
            
        ua=UserAgent()
        headers = {
            "Accept"            : "application/json",
            "accept-language"   : "en-US,en;q=0.9",
            "Content-type"      : "application/json",
            "Connection"        : "keep-alive",
            "priority"          : "u=1, i",
            "Accept-encoding"   : "gzip, deflate, br, zstd",
            "sec-ch-ua"         : ua.random,          # Use a random fake user-agent
            "sec-ch-ua-mobile"  : "?1",
            "sec-ch-ua-platform": "android",        # Optional: Customize the platform as needed
            "sec-fetch-dest"    : "empty",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-site"    : "same-site",
            "Referer"           : hd.get("Referer", ""),
            "Origin"            : hd.get("Origin", ""),  
            "Host"              : hd.get("Host", ""),    
        }
   
        return headers
    
    def header2():
        ua=UserAgent()
        headers = {
            "Accept"            : "application/json",
            "accept-language"   : "en-US,en;q=0.9",
            "Content-type"      : "application/json",
            "Connection"        : "keep-alive",
            "priority"          : "u=1, i",
            "Accept-encoding"   : "gzip, deflate, br, zstd",
            "sec-ch-ua"         : ua.random,          # Use a random fake user-agent
            "sec-ch-ua-mobile"  : "?1",
            "sec-ch-ua-platform": "android",        # Optional: Customize the platform as needed
            "sec-fetch-dest"    : "empty",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-site"    : "same-site",
            "Referer"           : "https://miniapp.bool.network/",
            "Origin"            : "https://miniapp.bool.network",  
            "Host"              : "bot-api.bool.network",    
        }
        return headers
    def get(self,url,token,data):
        return requests.get(url, headers=Api.header(token), json=data) 
    
    def get2(self,url,token,data):
        return requests.get(url, headers=Api.header2(), json=data) 
    
    def post(self,url,token,data):
 
        return requests.post(url, headers=Api.header(token), json=data) 
    
    def put(self,url,token,data):
        return requests.put(url, headers=Api.header(token), json=data) 
    
    def patch(url,token,data):
        return requests.patch(url, headers=Api.header(token), json=data) 





        