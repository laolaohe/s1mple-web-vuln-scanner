# s1mple-web-vuln-scanner
S1mple-Web-Scan一款基于插件化架构的轻量级 Web 自动化渗透测试原型逻辑实现

0x01 项目深度背景在现代 DevSecOps 流程中，自动化漏洞扫描是安全左移的关键。本项目是对自动化扫描器底层逻辑的复现与思考。通过本项目，我深入研究了：爬虫去噪与规范化逻辑（URL Normalization）。无回显漏洞的判定算法（基于时间差异分析的检测模型）。插件化解耦设计（面向对象多态在扫描引擎中的应用）。

0x02 核心技术架构项目采用“生产-消费”模型思想，将资产搜集与漏洞检测彻底解耦：Core Engine (调度中心)：负责协调 Reporter、Crawler 与 Plugin 之间的数据流转，采用接口抽象化设计。Asset Crawler (资产引擎)：Context-Aware：支持对 <form>、<input>、<textarea> 等多种交互元素的深度解析。Same-Origin Policy：严格限制扫描范围，防止请求越权至第三方域名。Vulnerability Plugins (检测算子)：SQLi Detector：实现 Error-based 与 Time-based (TDA) 双重检测。XSS Detector：基于响应流的回显匹配算法，支持 Context 语义分析。Path Discovery：基于非重定向（allow_redirects=False）状态码判定的隐蔽扫描。

0x03 技术难点攻克：TDA 检测模型针对 SQL 盲注，本项目放弃了传统的单一延时判定，引入了 TDA 时间差异分析：基准线测定：首先发送 sleep(0) 获取当前网络抖动下的基础响应时延 $T_{base}$。偏移量对比：注入 sleep(5) Payload，获取 $T_{target}$。判定公式：当 $T_{target} - T_{base} \ge 5$ 且连续三次波动率 $< 15\%$ 时，判定为高危注入。0x04 规范化报告输出 (JSON)为了适配大厂的安全流水线逻辑，本工具支持结构化 JSON 输出，方便与 SOC 平台或 Jira 系统集成。
{
  "vul_type": "SQL Injection (Time-based)",
  "url": "http://example.com/api/user",
  "payload": "sleep(5)",
  "description": "检测到时间盲注，基准延迟 0.1s，注入延迟 5.1s",
  "timestamp": "2024-03-20 22:00:00"
}

0x05 快速复现Bash#
克隆仓库
git clone https://github.com/your-id/sentinel-scanner.git




