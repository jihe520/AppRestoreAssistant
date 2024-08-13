import sys
import json
import os
import psutil
import win32process
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QScrollArea, QFrame, QLabel, QSizePolicy
)
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from PyQt6.QtGui import QCloseEvent
import pygetwindow as gw
from messagebar import MessageBar


class AppManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("应用管理器")
        self.setGeometry(100, 100, 400, 500)
        self.configs = {}
        self.load_configs()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()

        self.config_name_input = QLineEdit(self)
        self.config_name_input.setPlaceholderText("命名当前配置")
        top_layout.addWidget(self.config_name_input)

        self.save_button = QPushButton('保存', self)
        self.save_button.clicked.connect(self.check_and_save_config)
        top_layout.addWidget(self.save_button)

        main_layout.addLayout(top_layout)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setSpacing(0)
        self.scroll_content.setLayout(self.scroll_layout)

        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)
        self.populate_configs()

    def check_and_save_config(self):
        config_name = self.config_name_input.text()

        if not config_name:
            self.show_message_bar("请命名当前配置")
            return

        if config_name in self.configs:
            self.show_message_bar("该配置名称已经存在，请使用其他名称")
            return

        self.record_apps()
        self.add_config()
        self.save_to_json()

    def add_config(self):
        config_name = self.config_name_input.text()

        config_layout = QHBoxLayout()

        config_item = QLabel(config_name)
        config_item.setAlignment(Qt.AlignmentFlag.AlignCenter)
        config_layout.addWidget(config_item)

        restore_button = QPushButton('恢复', self)
        restore_button.clicked.connect(lambda: self.restore_apps(config_name))
        config_layout.addWidget(restore_button)

        delete_button = QPushButton('删除', self)
        delete_button.clicked.connect(lambda: self.remove_config(config_name, config_widget))
        config_layout.addWidget(delete_button)

        config_widget = QFrame()
        config_widget.setLayout(config_layout)

        size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        config_widget.setSizePolicy(size_policy)

        self.scroll_layout.insertWidget(0, config_widget)

        self.scroll_layout.update()
        self.scroll_layout.invalidate()

        self.config_name_input.clear()

    def record_apps(self):
        config_name = self.config_name_input.text()
        if not config_name:
            self.show_message_bar("请命名当前配置")
            return

        app_list = []
        recorded_exes = set()
        open_windows = gw.getAllWindows()

        current_pid = os.getpid()

        for window in open_windows:
            if window.title:
                hwnd = window._hWnd
                try:
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    if pid == current_pid:
                        continue

                    process_info = None
                    for proc in psutil.process_iter(['pid', 'name', 'exe']):
                        if proc.pid == pid:
                            process_info = proc.info
                            break

                    if process_info and process_info['exe'] not in recorded_exes:
                        if not process_info['exe'].startswith("C:\\Windows\\System32"):
                            app_list.append({
                                'title': window.title,
                                'exe': process_info['exe'],
                                'pid': process_info['pid']
                            })
                            recorded_exes.add(process_info['exe'])
                except Exception as e:
                    print(f"Error retrieving process for window '{window.title}': {str(e)}")

        if not app_list:
            print("No applications recorded. app_list is empty.")
            self.show_message_bar("未找到任何打开的应用。")
            return

        self.configs[config_name] = app_list

#  返回一个当前所有窗口应用中的exe路径，保存为一个list
    def get_open_windows(self):
        open_windows = gw.getAllWindows()
        new_list = []
        for window in open_windows:
            if window.title:
                hwnd = window._hWnd
                try:
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    process_info = None
                    for proc in psutil.process_iter(['pid', 'name', 'exe']):
                        if proc.pid == pid:
                            process_info = proc.info
                            break
                    if process_info:
                        new_list.append(process_info['exe'])
                except Exception as e:
                    print(f"Error retrieving process for window '{window.title}': {str(e)}")
        return new_list
        
    #  恢复应用
    def restore_apps(self, config_name):
        if not config_name:
            self.show_message_bar("请先选择要恢复的配置")
            return

        if config_name not in self.configs:
            self.show_message_bar("未找到指定配置")
            return
        
        apps = self.configs[config_name]
        # 获取当前所有软件
        # 与apps里面的对比，当apps里面不存在的时候，启动
        
        for app in apps:
            exe_path = app['exe']
            if exe_path not in self.get_open_windows():
                try:
                    os.startfile(exe_path)
                    print(f" {app['title']} is Opened")
                except Exception as e:
                    print(f"Error starting application {exe_path}: {str(e)}")
            else:
                print(f"Application {exe_path} is already running")

        self.show_message_bar("应用程序已恢复。")

    def remove_config(self, config_name, config_widget):
        if config_name in self.configs:
            del self.configs[config_name]

        self.scroll_layout.removeWidget(config_widget)
        config_widget.deleteLater()

    def load_configs(self):
        if os.path.exists("recorded_apps.json"):
            with open("recorded_apps.json", "r") as f:
                self.configs = json.load(f)
        else:
            self.configs = {}

    def populate_configs(self):
        for config_name in self.configs.keys():
            self.config_name_input.setText(config_name)
            self.add_config()

    def save_to_json(self):
        with open("recorded_apps.json", "w") as f:
            json.dump(self.configs, f, indent=4)

    def show_message_bar(self, message):
        self.message_bar = MessageBar(message, parent=self)
        self.message_bar.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.SubWindow)
        self.message_bar.setGeometry(self.geometry().width() // 4, -self.message_bar.height(), self.geometry().width() // 2, 40)
        self.message_bar.show_message()

    def closeEvent(self, event: QCloseEvent):
        self.save_to_json()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppManager()
    ex.show()
    sys.exit(app.exec())
