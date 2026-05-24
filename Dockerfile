# 使用 Python 3.11 官方镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制后端代码
COPY backend/ ./backend/

# 安装依赖
RUN pip install --no-cache-dir -r backend/requirements.txt

# 复制前端代码
COPY frontend/ ./frontend/

# 暴露端口
EXPOSE 8000

# 启动命令
CMD cd backend && uvicorn main:app --host 0.0.0.0 --port 8000
