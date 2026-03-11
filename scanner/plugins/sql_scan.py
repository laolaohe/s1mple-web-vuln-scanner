import requests
import time # [cite: 3, 7]
from plugins.base import BasePlugin # 

class SqlScan(BasePlugin): # 
    def __init__(self): # 
        self.name = "SQL Injection Scanner" # 

        self.payloads = ["'", "\"", "' OR 1=1--", "sleep(5)"] # 


    def scan(self, url, forms, reporter): # [cite: 3, 15]
        print(f"[*] 正在扫描 SQL 注入: {url}") # 
        for form in forms: # 
            for payload in self.payloads: # 
            
                data = {input_name: payload for input_name in form['inputs']} # 
                
                try:
                
                    start_time = time.time() # 
                    
                    if form['method'] == 'post': # 
                        res = requests.post(form['url'], data=data, timeout=10) # 
                    else: # 
                        res = requests.get(form['url'], params=data, timeout=10) # 
                    
               
                    duration = time.time() - start_time # 
                    
                 
                    if "SQL syntax" in res.text or "mysql_fetch" in res.text: # 
            
                        reporter.add_finding(
                            vul_type="SQL Injection (Error-based)",
                            url=form['url'],
                            payload=payload,
                            description="响应内容包含数据库语法错误关键字。"
                        ) 
                        print(f"[!!!] 发现 SQL 注入漏洞! URL: {form['url']} Payload: {payload}") # [cite: 6]
 
                    elif "sleep" in payload and duration >= 5: # [cite: 3, 4]
                        reporter.add_finding(
                            vul_type="SQL Injection (Time-based)",
                            url=form['url'],
                            payload=payload,
                            description=f"检测到时间盲注，请求耗时 {duration:.2f} 秒。"
                        ) # 
                        print(f"[!!!] 发现时间型 SQL 注入! URL: {form['url']}")

                except Exception as e: # [cite: 11]
                    pass # [cite: 11]