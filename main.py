import sys
from PySide2.QtWidgets import (QMainWindow, QApplication, QAction)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Slot
from buttons import CalcWidget


class MyApplication(QMainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.setWindowTitle("QCalculator")
        self.icon = QIcon('calc_icon.png')
        self.setWindowIcon(self.icon)
        self.max_size = (300, 300)
        self.resize(*self.max_size)
        self.setMaximumSize(*self.max_size)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')

        # Exit Action
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        self.file_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close_app)

        butts = CalcWidget()
        self.setCentralWidget(butts)

    @Slot()
    def close_app(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyApplication()
    # w.resize(300, 400)
    w.show()
    sys.exit(app.exec_())
