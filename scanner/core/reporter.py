# core/reporter.py
import json
import datetime

class Reporter:
    def __init__(self):
        self.results = []

    def add_finding(self, vul_type, url, payload, description):
        finding = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": vul_type,
            "url": url,
            "payload": payload,
            "description": description
        }
        self.results.append(finding)
        print(f"[!] 记录漏洞: {vul_type} 于 {url}")

    def save_to_file(self, filename="report.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=4, ensure_ascii=False)
        print(f"[*] 报告已保存至: {filename}")