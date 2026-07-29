<h1 align="center">🚀 NovaServe</h1>

<p align="center">
  <em>A lightweight, high-performance API backend designed for rapid local deployment and seamless scalability.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/fastapi-0.115+-green.svg" alt="FastAPI Version">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Status">
</p>

---

## 📖 Overview

NovaServe is a production-ready FastAPI boilerplate that follows a clean layered architecture pattern. It provides a solid foundation for building RESTful APIs with built-in support for global exception handling, CORS middleware, health checks, and environment-based configuration — all ready to run with a single command.

## ✨ Core Features

- **🏗️ Layered Architecture** — Clean separation of concerns with `api`, `core`, `services`, and `models` layers for maintainable and scalable code.
- **🛡️ Global Exception Handling** — Unified error responses across the entire application with custom business exceptions.
- **🌍 CORS Middleware** — Pre-configured Cross-Origin Resource Sharing for seamless frontend integration.
- **💚 Health Check** — Built-in `/api/v1/health` endpoint for monitoring and orchestration tools.
- **⚙️ Environment Configuration** — Centralized settings management via `pydantic-settings` with `.env` file support.
- **📦 Generic Response Models** — Consistent API response format with `ApiResponse<T>` and `PaginatedResponse<T>` generics.
- **📝 Comprehensive Type Hints** — Full type annotations throughout the codebase for better IDE support and code safety.
- **📜 Clear Chinese Documentation** — All modules are thoroughly commented in Chinese for developers in the Chinese-speaking community.

## 🛠️ Tech Stack

| Category          | Technology                                              |
| ----------------- | ------------------------------------------------------- |
| **Framework**     | [FastAPI](https://fastapi.tiangolo.com/) 0.115+          |
| **Server**        | [Uvicorn](https://www.uvicorn.org/) 0.34+                |
| **Validation**    | [Pydantic](https://docs.pydantic.dev/) 2.10+             |
| **Settings**      | [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) 2.7+ |
| **Language**      | Python 3.10+                                            |

## 📂 Project Structure

```
nova-serve/
├── api/                        # API 路由层 (Route Layer)
│   ├── __init__.py
│   └── health.py               # Health check endpoint
├── core/                       # 核心配置与基础设施 (Core Layer)
│   ├── __init__.py
│   ├── config.py               # Application settings & env config
│   └── exceptions.py           # Custom exceptions & global handlers
├── models/                     # 数据模型层 (Data Model Layer)
│   ├── __init__.py
│   └── base.py                 # Generic API response models
├── services/                   # 业务服务层 (Business Service Layer)
│   ├── __init__.py
│   └── base_service.py         # Base service with logging support
├── main.py                     # Application factory & entry point
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
└── README.md                   # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.10** or higher
- **pip** (Python package installer)
- (Optional) **virtualenv** or **venv** for isolated environments

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/york810327-rgb/nova-serve.git
cd nova-serve

# 2. Create and activate a virtual environment (recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env    # Copy and edit .env as needed
```

### Run the Server

```bash
# Start the development server with hot-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Once running, open your browser and visit:

- **Health Check**: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)
- **Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Quick Test

```bash
# Test the health check endpoint
curl http://localhost:8000/api/v1/health
```

Expected response:

```json
{
  "status": "ok",
  "app": "NovaServe",
  "version": "1.0.0",
  "timestamp": "2026-07-29T03:00:00.000000+00:00"
}
```

## ⚙️ Configuration

All settings are managed through environment variables or the `.env` file. See `.env.example` for a complete list of available options.

| Variable          | Default             | Description                  |
| ----------------- | ------------------- | ---------------------------- |
| `APP_NAME`        | `NovaServe`         | Application name             |
| `APP_VERSION`     | `1.0.0`             | Application version          |
| `DEBUG`           | `True`              | Debug mode (set to `False` in production) |
| `HOST`            | `0.0.0.0`           | Server host                  |
| `PORT`            | `8000`              | Server port                  |
| `API_PREFIX`      | `/api/v1`           | Global API route prefix      |
| `LOG_LEVEL`       | `INFO`              | Logging level                |

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  <sub>Built with ❤️ using Python & FastAPI</sub>
</p>
