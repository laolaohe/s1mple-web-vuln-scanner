import sys
import os

from core.crawler import Crawler
from core.engine import ScannerEngine
from core.reporter import Reporter

def main():
  
    target = "https://www.ruankao.org.cn/" 
    
    print(f"--- 漏洞扫描器启动: {target} ---")

    # 1. 初始化报告器
    reporter = Reporter()
    
    # 2. 爬取阶段
    crawler = Crawler(target)
    links, forms = crawler.run()
    
    if not links and not forms:
        print("[!] 未发现可扫描的目标，请检查 URL 是否可达。")
        return

    # 3. 扫描阶段
    engine = ScannerEngine(reporter)
    

    engine.run(links, forms)

    # 4. 报告保存阶段
    report_name = "my_scan_report.json"
    reporter.save_to_file(report_name)
    
    print(f"\n--- 扫描完成 ---")
    print(f"报告已生成至: {os.path.abspath(report_name)}")

if __name__ == "__main__":
    main()