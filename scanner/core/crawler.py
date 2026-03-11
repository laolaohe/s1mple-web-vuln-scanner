import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class Crawler:
    def __init__(self, base_url, max_depth=2): 
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited_urls = set()
        self.forms = []
        self.max_depth = max_depth
      
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def _parse_content(self, url, html):
        """解析页面内容：提取链接和表单 (内部方法)"""
        soup = BeautifulSoup(html, 'html.parser')
        
   
        page_forms = []
        for form in soup.find_all('form'):
            action = form.get('action')
            method = form.get('method', 'get').lower()
            inputs = form.find_all(['input', 'textarea', 'select']) 
            
            form_info = {
                'url': urljoin(url, action) if action else url,
                'method': method,
                'inputs': [i.get('name') for i in inputs if i.get('name')]
            }
            page_forms.append(form_info)

     
        page_links = set()
        for a in soup.find_all('a', href=True):
            full_url = urljoin(url, a['href']).split('#')[0] 
            if self.domain == urlparse(full_url).netloc:
                page_links.add(full_url)
        
        return page_links, page_forms

    def run(self):
        """优化后的爬取逻辑：一次请求，双重解析"""
        print(f"[*] 开始爬取: {self.base_url}")
       
        urls_to_visit = [(self.base_url, 0)]
        
        while urls_to_visit:
            current_url, depth = urls_to_visit.pop(0)
            
            if current_url in self.visited_urls or depth > self.max_depth:
                continue
                
            try:
                self.visited_urls.add(current_url)
                print(f"[+] 正在分析 ({depth}/{self.max_depth}): {current_url}")
                
              
                response = requests.get(current_url, headers=self.headers, timeout=5)
                if response.status_code != 200:
                    continue
                
              
                links, forms = self._parse_content(current_url, response.text)
                
                if forms:
                    self.forms.extend(forms)
                
                for link in links:
                    if link not in self.visited_urls:
                        urls_to_visit.append((link, depth + 1))
                        
            except Exception as e:
                print(f"[!] 访问 {current_url} 失败: {e}")
        
        return self.visited_urls, self.forms