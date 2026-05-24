"""
最简单的后端 API
功能：接收一个名字，返回问候语
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

# 创建应用
app = FastAPI(title="简单全栈示例")

# 允许前端访问（CORS）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（开发时方便）
    allow_methods=["*"],
    allow_headers=["*"],
)


# 数据模型（定义请求格式）
class NameRequest(BaseModel):
    name: str


class GreetingResponse(BaseModel):
    message: str
    status: str


# 模拟数据库：用户余额
user_balance = 100


# 接口 1：GET 请求，测试用
@app.get("/api/")
def home():
    return {"message": "后端运行正常！", "status": "ok"}


# 接口 2：GET 请求，接收名字返回问候
@app.get("/api/greet", response_model=GreetingResponse)
def greet(name: str):
    """
    接收一个名字，返回问候语
    例如：/greet?name=张三 → {"message": "你好，张三！", "status": "success"}
    """
    return GreetingResponse(
        message=f"你好，{name}！",
        status="success"
    )


# 接口 3：GET 请求，获取当前时间
@app.get("/api/time")
def get_time():
    from datetime import datetime
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "ok"
    }


# 接口 4：GET 请求，查询余额（安全）
@app.get("/api/balance")
def get_balance():
    return {"balance": user_balance}


# 接口 5：POST 请求，充值（安全！用 POST 写数据）
class MoneyRequest(BaseModel):
    amount: int

@app.post("/api/add-money")
def add_money(request: MoneyRequest):
    """
    ✅ 安全示例：用 POST 修改数据
    <img> 标签无法触发 POST 请求
    """
    global user_balance
    user_balance += request.amount
    return {"message": f"充值成功！余额：{user_balance}", "balance": user_balance}


# 挂载前端静态文件（部署时使用）
# 检查 frontend 目录是否存在
frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')
if os.path.exists(frontend_path):
    # 部署模式：后端托管前端
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")
    
    @app.get("/")
    async def serve_frontend():
        return FileResponse(os.path.join(frontend_path, 'index.html'))
    
    print("✅ 前后端一起部署模式")
else:
    print("⚠️ 仅后端部署模式（frontend 目录不存在）")

if __name__ == "__main__":
    import uvicorn
    print("启动服务器...")
    print("访问地址：http://localhost:8000")
    print("API 文档：http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
