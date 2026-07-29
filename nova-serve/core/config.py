"""
NovaServe - 应用配置模块
=====================
基于 Pydantic Settings 管理所有环境变量和应用配置。
支持从 .env 文件自动加载配置项。
"""

from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    全局应用配置类。

    所有配置项均可通过环境变量或 .env 文件设置。
    配置项名称大小写敏感，环境变量自动映射为对应的大写形式。
    """

    # ---------- 应用基本信息 ----------
    APP_NAME: str = "NovaServe"  # 应用名称
    APP_VERSION: str = "1.0.0"   # 应用版本号
    DEBUG: bool = True           # 调试模式开关（生产环境请设为 False）

    # ---------- 服务配置 ----------
    HOST: str = "0.0.0.0"        # 服务监听地址
    PORT: int = 8000             # 服务监听端口
    API_PREFIX: str = "/api/v1"  # 全局 API 路由前缀

    # ---------- CORS 跨域配置 ----------
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",   # 默认允许前端开发服务器
        "http://localhost:8080",   # 默认允许其他本地前端
    ]
    CORS_ALLOW_CREDENTIALS: bool = True        # 允许携带凭据（Cookie）
    CORS_ALLOW_METHODS: List[str] = ["*"]      # 允许所有 HTTP 方法
    CORS_ALLOW_HEADERS: List[str] = ["*"]      # 允许所有请求头

    # ---------- 日志配置 ----------
    LOG_LEVEL: str = "INFO"  # 日志级别：DEBUG / INFO / WARNING / ERROR

    # ---------- Pydantic 配置 ----------
    model_config = SettingsConfigDict(
        env_file=".env",          # 从项目根目录的 .env 文件加载
        env_file_encoding="utf-8",  # 环境文件编码
        case_sensitive=True,       # 配置项名称大小写敏感
        extra="ignore",            # 忽略未定义的环境变量
    )


# ---------- 全局配置单例 ----------
# 项目中任何模块均可通过 `from core.config import settings` 直接使用
settings: Settings = Settings()