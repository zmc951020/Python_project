# Google Drive 备份配置

## 创建 OAuth 凭据
- 打开 https://console.cloud.google.com/ 并登录
- 创建项目
  - **注意**：Google Cloud 项目名称不支持下划线 `_`，建议使用 `python-project` 或 `pythonbackup`。这只是云端项目的标识，不影响本地代码运行。
- 进入 “API 和服务 → OAuth 同意屏幕”，将用户类型设为外部，并至少填写应用名称与支持邮箱
- 在 “凭据 → 创建凭据 → OAuth 客户端 ID”，选择 “桌面应用”，下载得到 `client_secret_xxx.json`
- 将该文件重命名为 `google_credentials.json` 放到项目根目录

## 安装依赖
- 在终端运行：`pip install -r requirements.txt`

## 首次授权
- 在终端运行：`python -m src.modules.google_drive_backup`
- 浏览器会弹出授权页面，选择账号并允许权限
- 授权完成后在项目根目录生成 `google_token.json`

## 使用
- 代码中调用：
  - 
    ```
    from src.modules.google_drive_backup import run_backup
    path, file_id = run_backup()
    ```
- 可传 `folder_id` 将文件上传到指定 Drive 目录

## Git 与备份联动
- 可在 `.git/hooks/post-commit` 中调用：
  - 
    ```
    python -m src.modules.google_drive_backup
    ```
- 钩子仅在本地生效，不会被提交

## 安全
- `google_credentials.json` 与 `google_token.json` 已加入 `.gitignore`
- 请勿将任何密钥文件提交到远程仓库
