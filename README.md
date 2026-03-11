# s1mple-web-vuln-scanner
一个基于 Python 实现的轻量级 Web 漏洞扫描器，通过爬虫收集站点信息，并利用插件化扫描模块检测常见 Web 安全漏洞。
该工具实现了从 信息收集 → 漏洞检测 → 报告生成 的完整流程，适合用于学习 Web 安全扫描原理以及安全工具开发。

项目功能
1 网站爬虫（Crawler）
自动爬取目标网站页面并提取：页面链接（Links）/表单信息（Forms）
特性：
同域名限制，避免爬取外部站点
深度限制防止死循环
自动解析 HTML 表单
自动提取 GET / POST 参数
使用库：
requests
BeautifulSoup

2 漏洞扫描引擎（Scanner Engine）
扫描引擎负责：
调度所有扫描插件
对 URL 和表单进行分类扫描
统一管理漏洞结果
支持插件化设计：

ScannerEngine
│
├── SQL Injection Scanner
├── XSS Scanner
└── Directory Scanner

已实现漏洞检测
1 SQL Injection 扫描
检测方式：
Error-Based SQL Injection
通过 Payload 触发数据库错误信息，例如：

'
"
' OR 1=1--

检测响应中是否出现：
SQL syntax
mysql_fetch
如果出现则可能存在 SQL 注入漏洞。

Time-Based SQL Injection
使用 Payload：
sleep(5)
如果服务器响应时间 ≥ 5 秒，则可能存在时间盲注。

实现原理：
start_time = time.time()
requests.get(...)
duration = time.time() - start_time
2 XSS 漏洞扫描
原理：
向表单输入恶意 JavaScript Payload，例如：
<script>alert(1)</script>
如果 Payload 在响应页面中未被过滤，可能存在 反射型 XSS。

3 敏感目录扫描
使用简单字典扫描常见敏感路径：

/admin
/login
/config
/.git
/backup
/uploads
/test

通过 HTTP 状态码判断：200/301/403

如果存在则记录为 敏感路径泄露。

报告系统

扫描结果会被记录到 Reporter 模块，并生成 JSON 报告。
示例：
[
  {
    "timestamp": "2026-03-10 14:32:11",
    "type": "SQL Injection",
    "url": "http://example.com/login",
    "payload": "' OR 1=1--",
    "description": "响应内容包含数据库语法错误关键字"
  }
]

输出文件：
my_scan_report.json
项目结构
web-vuln-scanner
│
├── main.py                 # 主程序入口
│
├── core
│   ├── crawler.py          # 网站爬虫
│   ├── engine.py           # 扫描引擎
│   └── reporter.py         # 报告模块
│
├── plugins
│   ├── base.py             # 插件基类
│   ├── sql_scan.py         # SQL 注入扫描
│   ├── xss_scan.py         # XSS 扫描
│   └── dir_scan.py         # 目录扫描




