import sys
from calculator import Calculator
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowTitle("Taschenrechner")
        icon = QIcon('calc_icon.png')
        self.setWindowIcon(icon)
        c = Calculator()
        c.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec_())
