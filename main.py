import sys
from calculator import Calculator
from PySide2.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Calculator()
    w.show()
    sys.exit(app.exec_())
