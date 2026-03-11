# plugins/base.py
class BasePlugin:
    def __init__(self):
        self.name = "Base Plugin"

    def scan(self, url, params=None):
        """
        所有插件必须实现此方法
        :param url: 目标 URL
        :param params: 表单参数列表或其他必要信息
        """
        raise NotImplementedError("子类必须实现 scan 方法")