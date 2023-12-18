from pathlib import Path

import qdarktheme


def main():
    import sys
    from app import app
    from auth import Login

    auth_window = Login()
    auth_window.show()

    #dark_palette = qdarktheme.load_palette()
    #app.setPalette(dark_palette)
    #app.setStyleSheet(Path('style.сss').read_text())

    def close_all_windows():
        for widget in app.topLevelWidgets():
            widget.close()

    app.aboutToQuit.connect(close_all_windows)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
