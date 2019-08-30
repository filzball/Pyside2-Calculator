import sys
import os
from calculator import Calculator
from PySide2.QtWidgets import QApplication


def resource_path(relative_path):
    """ Get absolute path to resource,
    works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Logo = resource_path("calc_icon.png")
    w = Calculator(Logo)
    w.show()
    sys.exit(app.exec_())
