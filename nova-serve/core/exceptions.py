"""
NovaServe - 全局异常处理模块
========================
定义项目统一的自定义异常类及全局异常处理器，
确保所有异常以一致的 JSON 格式返回给客户端。
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from typing import Optional, Any


class NovaServeException(Exception):
    """
    项目自定义基础异常类。

    所有业务层异常应继承此类，以便全局异常处理器统一捕获。

    Attributes:
        status_code (int): HTTP 状态码
        code (int): 业务错误码
        message (str): 错误描述信息
        detail (Optional[Any]): 额外的错误详情（开发调试用）
    """

    def __init__(
        self,
        status_code: int = 400,
        code: int = 1000,
        message: str = "业务处理异常",
        detail: Optional[Any] = None,
    ) -> None:
        self.status_code: int = status_code
        self.code: int = code
        self.message: str = message
        self.detail: Optional[Any] = detail
        super().__init__(message)


class NotFoundException(NovaServeException):
    """404 - 资源未找到异常"""

    def __init__(self, message: str = "请求的资源不存在") -> None:
        super().__init__(status_code=404, code=1001, message=message)


class ValidationException(NovaServeException):
    """422 - 请求参数验证失败异常"""

    def __init__(self, message: str = "请求参数验证失败") -> None:
        super().__init__(status_code=422, code=1002, message=message)


class UnauthorizedException(NovaServeException):
    """401 - 未授权异常"""

    def __init__(self, message: str = "未授权访问，请先登录") -> None:
        super().__init__(status_code=401, code=1003, message=message)


class ForbiddenException(NovaServeException):
    """403 - 禁止访问异常"""

    def __init__(self, message: str = "没有权限执行此操作") -> None:
        super().__init__(status_code=403, code=1004, message=message)


# ---------- 全局异常处理器 ----------

async def nova_serve_exception_handler(
    request: Request, exc: NovaServeException
) -> JSONResponse:
    """
    统一处理所有 NovaServeException 及其子类异常。

    将所有自定义异常转换为统一的 JSON 错误响应格式，
    方便前端进行统一的错误处理。

    Args:
        request: FastAPI 请求对象（用于记录请求路径等信息）
        exc: 被捕获的 NovaServeException 实例

    Returns:
        JSONResponse: 包含错误码、消息及详情的 JSON 响应
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.code,
            "message": exc.message,
            "detail": exc.detail,
        },
    )