import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dark Title Bar Example")
        self.setGeometry(100, 100, 800, 600)

        # Создаем виджет верхней части окна
        top_widget = QLabel("Your custom content here")
        top_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Добавляем виджет верхней части окна в вертикальный лейаут
        layout = QVBoxLayout()
        layout.addWidget(top_widget)

        # Устанавливаем вертикальный лейаут в качестве основного лейаута для центрального виджета
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Устанавливаем стиль для изменения фона заголовка окна
        style_sheet = """
            QHeaderView::section {
                background-color: #2c3e50; /* Цвет фона заголовка окна */
                color: white; /* Цвет текста заголовка окна */
            }
        """
        self.setStyleSheet(style_sheet)

if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyMainWindow()
    window.show()
    app.exec()