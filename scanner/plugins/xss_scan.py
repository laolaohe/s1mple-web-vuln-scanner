import requests
from .base import BasePlugin # 

class XssScan(BasePlugin): # 
    def __init__(self): # 
        self.name = "XSS Scanner" # 
        self.payloads = [
            "<script>alert('xss')</script>",
            "\"'><script>alert(1)</script>",
            "<img src=x onerror=alert(1)>"
        ] # 


    def scan(self, url, forms, reporter): # 
        print(f"[*] 正在执行 XSS 扫描...") # 
        for form in forms: # 
            for payload in self.payloads: # 
    
                data = {input_name: payload for input_name in form['inputs']} # 
                
                try:
                  
                    if form['method'] == 'post':
                        res = requests.post(form['url'], data=data, timeout=5) # 
                    else:
                        res = requests.get(form['url'], params=data, timeout=5) # 
                    
                
                    if payload in res.text: # 
               
                        reporter.add_finding(
                            vul_type="XSS", 
                            url=form['url'], 
                            payload=payload, 
                            description="发现反射型 XSS 漏洞，用户输入未被过滤直接渲染"
                        ) 
                        
                        print(f"[!!!] 发现反射型 XSS 漏洞!") # 
                        print(f"      URL: {form['url']}") # 
                        print(f"      Payload: {payload}") # 
                        
                except Exception as e:
                    print(f"[!] 扫描异常: {e}") 