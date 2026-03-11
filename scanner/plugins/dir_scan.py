import requests
from urllib.parse import urlparse # 新增：用于解析根域名
from .base import BasePlugin # 

class DirScan(BasePlugin): # 
    def __init__(self): # 
        self.name = "Directory Scanner" # 
      
        self.common_dirs = [
            "/admin", "/login", "/config", "/.git", "/backup", "/uploads", "/test"
        ] # 


    def scan(self, url, forms, reporter): # 
        print(f"[*] 正在进行目录扫描任务...") # 
        
  
        parsed_url = urlparse(url) # 
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}" # 
        
        print(f"[*] 基础扫描地址: {base_url}") # 

        for directory in self.common_dirs: # 
            target = base_url + directory # 
            try:
    
                res = requests.get(target, timeout=3, allow_redirects=False) # 
             
                if res.status_code in [200, 403, 301]: # 
                    if reporter: # 
                        reporter.add_finding(
                            vul_type="敏感路径泄露",
                            url=target,
                            payload=directory,
                            description=f"发现敏感路径，响应码: {res.status_code}"
                        ) # 
                    print(f"[+] 发现敏感路径: {target} (Status: {res.status_code})") # 
            except Exception: # 
                continue #