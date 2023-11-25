from pathlib import Path

from add import *
from auth import Login

import qdarktheme


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    dark_palette = qdarktheme.load_palette()
    link_color = dark_palette.link().color()
    link_rgb = link_color.getRgb()
    app.setPalette(dark_palette)
    app.setStyleSheet(Path('style.сss').read_text())

    auth_window = Login()
    auth_window.show()


    sys.exit(app.exec())
