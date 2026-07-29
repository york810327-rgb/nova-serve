"""
NovaServe - 基础服务层模块
=======================
所有业务服务类的抽象基类，提供通用的日志记录和
错误处理能力。具体业务服务应继承此类并实现自己的逻辑。
"""

import logging
from typing import Any

# ---------- 配置日志记录器 ----------
logger: logging.Logger = logging.getLogger(__name__)


class BaseService:
    """
    业务服务基类。

    封装通用的日志记录功能，为所有子类提供统一的日志输出方式。
    子类可直接使用 self.logger 记录日志，无需重新配置。

    使用示例:
        class UserService(BaseService):
            def get_user_by_id(self, user_id: int) -> dict:
                self.logger.info(f"查询用户: {user_id}")
                ...
    """

    def __init__(self) -> None:
        """初始化服务实例，绑定日志记录器。"""
        self.logger: logging.Logger = logger

    def log_info(self, message: str, *args: Any, **kwargs: Any) -> None:
        """
        记录 INFO 级别日志。

        Args:
            message: 日志消息内容
            *args: 格式化的位置参数
            **kwargs: 额外的关键字参数（如 exc_info=True 记录异常堆栈）
        """
        self.logger.info(message, *args, **kwargs)

    def log_warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        """
        记录 WARNING 级别日志。

        Args:
            message: 日志消息内容
            *args: 格式化的位置参数
            **kwargs: 额外的关键字参数
        """
        self.logger.warning(message, *args, **kwargs)

    def log_error(self, message: str, *args: Any, **kwargs: Any) -> None:
        """
        记录 ERROR 级别日志。

        Args:
            message: 日志消息内容
            *args: 格式化的位置参数
            **kwargs: 额外的关键字参数（如 exc_info=True 记录异常堆栈）
        """
        self.logger.error(message, *args, **kwargs)