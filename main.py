from pathlib import Path

from auth import Login
from PyQt6 import QtWidgets
import qdarktheme


if __name__ == "__main__":

    import sys

    from app import app

    #dark_palette = qdarktheme.load_palette()
    #link_color = dark_palette.link().color()
    #link_rgb = link_color.getRgb()
    #app.setPalette(dark_palette)
    #app.setStyleSheet(Path('style.сss').read_text())

    auth_window = Login()
    auth_window.show()


    def close_all_windows():
        for widget in app.topLevelWidgets():
            widget.close()


    app.aboutToQuit.connect(close_all_windows)

    sys.exit(app.exec())
