"""
NovaServe - 应用主入口模块
=======================
FastAPI 应用工厂，负责创建和配置整个应用实例。
包含全局异常处理、CORS 中间件、健康检查等功能。
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from core.config import settings
from core.exceptions import NovaServeException, nova_serve_exception_handler
from api.health import router as health_router


def create_app() -> FastAPI:
    """
    创建并配置 FastAPI 应用实例。

    Returns:
        FastAPI: 配置完成的应用实例
    """
    # ---------- 初始化 FastAPI 应用 ----------
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="A lightweight, high-performance API backend designed for rapid local deployment and seamless scalability.",
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
    )

    # ---------- 配置 CORS 跨域中间件 ----------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ---------- 注册全局异常处理器 ----------
    app.add_exception_handler(NovaServeException, nova_serve_exception_handler)

    # ---------- 注册全局 HTTP 异常处理 ----------
    @app.exception_handler(Exception)
    async def global_exception_handler(_request: Request, exc: Exception) -> JSONResponse:
        """捕获所有未处理的异常，统一返回 500 错误响应。"""
        return JSONResponse(
            status_code=500,
            content={
                "code": 500,
                "message": "服务器内部错误，请稍后重试",
                "detail": str(exc) if settings.DEBUG else None,
            },
        )

    # ---------- 注册路由 ----------
    app.include_router(health_router, prefix=settings.API_PREFIX)

    return app


# ---------- 创建应用实例（供 uvicorn 直接引用）----------
app: FastAPI = create_app()