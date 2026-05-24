# 🚀 部署到 Render（免费版）

## 📋 部署前准备

### 1. 注册账号
- 访问 https://render.com
- 用 GitHub 账号登录

### 2. 准备代码
确保以下文件已创建：
- `render.yaml` - Render 配置文件
- `backend/requirements.txt` - Python 依赖
- `backend/main.py` - 后端代码

---

## 🚀 部署步骤

### 第一步：推送到 GitHub

```bash
# 1. 进入项目目录
cd /Users/zhalijun/Desktop/全栈/simple-fullstack-app

# 2. 初始化 git（如果还没做）
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "准备部署到 Render"

# 5. 在 GitHub 创建新仓库，然后推送
git remote add origin https://github.com/你的用户名/simple-fullstack-app.git
git push -u origin main
```

---

### 第二步：在 Render 创建服务

1. 登录 https://dashboard.render.com
2. 点击 **New +** → **Web Service**
3. 选择你的 GitHub 仓库 `simple-fullstack-app`
4. 配置如下：

| 配置项 | 值 |
|--------|-----|
| Name | `simple-fullstack-app` |
| Runtime | `Python 3` |
| Build Command | `pip install -r backend/requirements.txt` |
| Start Command | `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT` |
| Plan | `Free` |

5. 点击 **Create Web Service**

---

### 第三步：等待部署完成

- 部署过程约 2-5 分钟
- 看到 "Your service is live" 表示成功
- 获得网址：`https://simple-fullstack-app.onrender.com`

---

## 🌐 访问你的应用

### 后端 API
```
https://simple-fullstack-app.onrender.com/
https://simple-fullstack-app.onrender.com/docs  (API 文档)
```

### 前端页面
需要额外部署前端，或者把前端打包到后端。

**简单方案**：用 Python 托管前端静态文件

---

## 🔧 进阶：前后端一起部署

修改 `backend/main.py`，添加静态文件服务：

```python
from fastapi.staticfiles import StaticFiles

# 挂载前端静态文件
app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")
```

然后重新部署。

---

## ⚠️ 免费版限制

| 限制 | 说明 |
|------|------|
| 15分钟休眠 | 无人访问15分钟后自动休眠 |
| 30秒冷启动 | 休眠后首次访问需等待30秒 |
| 每月100GB流量 | 超出后服务暂停 |

### 保持唤醒（可选）
用 UptimeRobot 每5分钟访问一次：
1. 注册 https://uptimerobot.com
2. 添加监控，输入你的网址
3. 设置每5分钟检查一次

---

## 📝 更新代码

每次修改代码后：
```bash
git add .
git commit -m "更新内容"
git push
```

Render 会自动重新部署！

---

## ❓ 常见问题

**Q: 部署失败怎么办？**  
A: 查看 Render 的 Logs 页面，检查错误信息

**Q: 如何查看日志？**  
A: Render 控制台 → 你的服务 → Logs

**Q: 可以自定义域名吗？**  
A: 免费版不支持，需升级到 $7/月

---

## 🎉 完成！

现在全世界都能访问你的全栈应用了！
