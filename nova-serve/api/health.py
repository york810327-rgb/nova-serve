"""
NovaServe - 健康检查路由模块
=======================
提供系统健康检查接口，用于监控服务运行状态。
"""

from fastapi import APIRouter
from datetime import datetime, timezone
from typing import Any

router: APIRouter = APIRouter(tags=["系统健康检查"])


@router.get(
    "/health",
    summary="服务健康检查",
    description="返回服务的当前运行状态、版本信息及服务器时间，用于负载均衡或监控系统的健康探测。",
)
async def health_check() -> dict[str, Any]:
    """
    健康检查接口。

    对外暴露 /api/v1/health，返回服务的基本状态信息。
    可用于 Kubernetes liveness probe、负载均衡健康检测等场景。

    Returns:
        Dict[str, Any]: 包含状态(status)、应用名称(app)、版本(version)、时间戳(timestamp)的字典
    """
    return {
        "status": "ok",
        "app": "NovaServe",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }