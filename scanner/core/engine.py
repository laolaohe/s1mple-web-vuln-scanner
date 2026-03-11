from plugins.sql_scan import SqlScan
from plugins.xss_scan import XssScan
from plugins.dir_scan import DirScan

class ScannerEngine:
    def __init__(self, reporter): # 初始化时接收报告器
        self.reporter = reporter
        # 
        self.plugins = [SqlScan(), XssScan(), DirScan()]

    def run(self, urls, forms):
        print("[*] 引擎开始工作...")
        
        for current_url in urls:
            for plugin in self.plugins:
                if isinstance(plugin, DirScan):
                    plugin.scan(current_url, None, self.reporter)

        if forms:
            for plugin in self.plugins:
                if not isinstance(plugin, DirScan):
                    base_target = forms[0]['url'] if forms else ""
                    plugin.scan(base_target, forms, self.reporter)