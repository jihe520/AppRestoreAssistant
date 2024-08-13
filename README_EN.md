
# AppRestoreAssistant 🚀

**Application Restore Assistant**

> [中文版](README.md)

Have you ever been frustrated by having to reopen all your applications after shutting down your computer? `AppRestoreAssistant` is designed to help you record all currently open applications and quickly restore them when you restart your computer, so you can get back to work instantly!

## Features ✨

- **Record all currently open applications** 📝
- **Restore all recorded applications upon startup** 🔄

## Dependencies 📦

- **System Libraries**:
  - `sys`
  - `json`
  - `os`

- **Third-Party Libraries**:
  - `psutil`: For system monitoring and process management
  - `win32process`: Python interface for Windows API, used for process management
  - `PyQt6`: Used for building the graphical user interface (GUI)
  - `pygetwindow`: Used for retrieving window information
  - `messagebar`: Used for displaying message bars

## Installation Guide 💻

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/jihe520/AppRestoreAssistant.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AppRestoreAssistant
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage 🚀

1. Directly download and run the packaged software:

   - Visit the [releases page](https://github.com/jihe520/AppRestoreAssistant/releases) to download the latest version.
   - Extract the files and run `AppRestoreAssistant.exe`.

   - Press the "Save State" button to save the current application state.
   - After restarting your computer, run `AppRestoreAssistant.exe` and press the "Restore State" button to reopen all recorded applications.

## Packaging Guide 📦

If you want to package the project into an executable, follow these steps:

1. Ensure that you have `PyInstaller` installed:

    ```bash
    pip install pyinstaller
    ```

2. Run the following command to package the application:

    ```bash
    pyinstaller -n "AppRestoreAssistant" -w app.py
    ```

   This will generate a standalone executable in the `dist` directory.

## Acknowledgments 🙏

Special thanks to the following projects and technologies for their support:

- [OpenAI](https://www.openai.com/) for GPT technology
- [deepseek](https://deepseek.com) for technical support

## Future Plans 🔧

- **View and modify each saved state configuration**: Enhance user customization options by allowing users to view and modify recorded applications and their configurations.
- **UI Optimization**: Improve the user interface design to make it more intuitive and user-friendly.

## Contributing 🙌

If you have any suggestions or find any issues, please submit an issue or pull request. We greatly welcome your contributions!


---

Thank you for using `AppRestoreAssistant`! We hope this tool makes your workflow more efficient! 😊