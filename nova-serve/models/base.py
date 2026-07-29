"""
NovaServe - 通用数据模型模块
=======================
定义项目中所有 API 接口共用的 Pydantic 响应模型，
确保所有接口返回格式统一。
"""

from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel, Field

# ---------- 泛型类型变量 ----------
T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """
    通用 API 响应模型（泛型）。

    所有成功响应均使用此模型进行包装，
    确保前端能够以统一的方式解析响应数据。

    Attributes:
        code (int): 业务状态码，0 表示成功
        message (str): 响应提示信息
        data (Optional[T]): 响应数据载荷，类型由泛型 T 决定

    使用示例:
        @router.get("/users/{user_id}", response_model=ApiResponse[UserSchema])
        async def get_user(user_id: int):
            user = user_service.get_user(user_id)
            return ApiResponse(data=user, message="查询成功")
    """

    code: int = Field(default=0, description="业务状态码，0 表示成功")
    message: str = Field(default="操作成功", description="响应提示信息")
    data: Optional[T] = Field(default=None, description="响应数据载荷")


class PaginatedResponse(ApiResponse[T]):
    """
    分页响应模型。

    在通用响应模型基础上增加了分页相关字段，
    适用于需要分页的列表查询接口。

    Attributes:
        page (int): 当前页码，从 1 开始
        page_size (int): 每页数据条数
        total (int): 数据总条数
        total_pages (int): 总页数
    """

    page: int = Field(default=1, ge=1, description="当前页码")
    page_size: int = Field(default=20, ge=1, le=100, description="每页数据条数")
    total: int = Field(default=0, ge=0, description="数据总条数")
    total_pages: int = Field(default=0, ge=0, description="总页数")