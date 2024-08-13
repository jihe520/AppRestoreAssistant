
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QRect

class MessageBar(QWidget):
    def __init__(self, message, duration=3000, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)
        self.setStyleSheet("background-color: #323232; color: white; font-size: 16px; border-radius: 5px;")

        layout = QHBoxLayout()
        self.label = QLabel(message, self)
        self.label.setStyleSheet("margin-left: 10px;")
        layout.addWidget(self.label)

        close_button = QPushButton("×", self)
        close_button.setStyleSheet("background: transparent; color: white; font-size: 18px;")
        close_button.setFixedSize(30, 30)
        close_button.clicked.connect(self.hide_message)
        layout.addWidget(close_button)

        self.setLayout(layout)

        self.animation_in = QPropertyAnimation(self, b"geometry")
        self.animation_in.setDuration(500)
        self.animation_out = QPropertyAnimation(self, b"geometry")
        self.animation_out.setDuration(500)

        self.timer = QTimer(self)
        self.timer.setInterval(duration)
        self.timer.timeout.connect(self.hide_message)

    def show_message(self):
        parent_geometry = self.parent().geometry()
        self.setGeometry(0, -self.height(), parent_geometry.width(), self.height())

        self.animation_in.setStartValue(self.geometry())
        self.animation_in.setEndValue(QRect(0, 0, parent_geometry.width(), self.height()))
        self.animation_in.start()

        self.show()  # 确保显示

        self.timer.start()

    def hide_message(self):
        parent_geometry = self.parent().geometry()
        self.animation_out.setStartValue(self.geometry())
        self.animation_out.setEndValue(QRect(0, -self.height(), parent_geometry.width(), self.height()))
        self.animation_out.finished.connect(self.deleteLater)
        self.animation_out.start()

        self.timer.stop()