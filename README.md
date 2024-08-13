# AppRestoreAssistant 🚀

**应用恢复助手**

> [English Version](README_EN.md)

经常因为软件开得太多，每次关机后重新打开所有应用，真的让人感到烦恼。`AppRestoreAssistant` 旨在帮助你记录当前所有打开的应用程序，并在你重新启动计算机后快速恢复这些应用程序，让你可以立即进入工作状态！

## 功能 ✨

- **记录当前所有打开的应用程序** 📝
- **在开机后恢复记录的所有应用程序** 🔄

## 依赖库 📦

- **系统库**:
  - `sys`
  - `json`
  - `os`

- **第三方库**:
  - `psutil`：用于系统监控和进程管理
  - `win32process`：Windows API 的 Python 接口，用于进程管理
  - `PyQt6`：用于构建图形用户界面 (GUI)
  - `pygetwindow`：用于获取窗口信息
  - `messagebar`：用于显示消息栏

## 安装指南 💻

1. 克隆这个仓库到本地：

    ```bash
    git clone https://github.com/jihe520/AppRestoreAssistant.git
    ```

2. 进入项目目录：

    ```bash
    cd AppRestoreAssistant
    ```

3. 创建并激活虚拟环境：

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

4. 安装依赖：

    ```bash
    pip install -r requirements.txt
    ```

## 使用方法 🚀

1. 直接下载打包后的软件并运行：

   - 访问 [发布页面](https://github.com/jihe520/AppRestoreAssistant/releases) 下载最新版本的打包文件。
   - 解压缩并运行 `AppRestoreAssistant.exe`。

   - 按下“记录状态”按钮来保存当前的应用状态。
   - 在计算机重新启动后，运行 `AppRestoreAssistant.exe` 并按下“恢复状态”按钮来重新打开所有记录的应用程序。

## 打包指南 📦

如果你希望自己打包项目为可执行文件，可以按照以下步骤操作：

1. 确保你已经安装 `PyInstaller`：

    ```bash
    pip install pyinstaller
    ```

2. 运行以下命令打包应用程序：

    ```bash
    pyinstaller -n "AppRestoreAssistant" -w app.py
    ```

   这会生成一个独立的可执行文件，位于 `dist` 目录中。

## 鸣谢 🙏

特别感谢以下项目和技术提供了支持：

- [OpenAI](https://www.openai.com/) 的 GPT 技术
- [deepseek](https://deepseek.com) 的技术支持

## 后续计划 🔧

- **查看和详细修改每个计划配置**：增强用户的自定义选项，允许用户查看和修改记录的应用程序及其配置。
- **优化界面**：改进用户界面的设计，使其更加直观和易于使用。

## 贡献 🙌

如果你有任何建议或发现了问题，请提交问题或拉取请求，我们非常欢迎你的贡献！


---

感谢使用 `AppRestoreAssistant`！希望这个工具能让你的工作流程更加高效！😊

以上 `ChatGPT` 生成
