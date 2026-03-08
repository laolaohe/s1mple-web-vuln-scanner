# s1mple-web-vuln-scanner
s1mple-web-vuln-scanner 是一个使用 Python 开发的轻量级 Web 漏洞扫描工具，用于自动化检测常见 Web 安全漏洞。

该项目主要用于安全学习与实践，通过模拟真实渗透测试中的信息收集与漏洞检测流程，实现对目标 Web 应用的基础安全检测能力。

当前版本主要支持对常见 Web 漏洞的检测，例如：

SQL 注入（SQL Injection）

XSS（跨站脚本攻击）

常见敏感路径扫描

基础信息收集

本项目旨在帮助安全学习者理解 Web 漏洞扫描器的基本实现原理，并提升安全开发与攻防实践能力。

功能特性

🔍 目标信息探测

自动识别网站状态码

获取页面标题（Title）

基础页面内容分析

💉 SQL 注入检测

基于 Payload 注入测试

根据返回内容判断异常

⚡ XSS 漏洞检测

自动构造 XSS Payload

检测反射型 XSS

📂 敏感路径扫描

扫描常见后台路径

常见敏感文件检测

🧠 模块化设计

方便扩展新的漏洞检测模块

技术栈

项目主要使用以下技术实现：

Python 3

requests —— HTTP 请求发送

BeautifulSoup —— 页面解析

argparse —— 命令行参数解析

threading —— 多线程扫描
