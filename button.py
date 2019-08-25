<<<<<<< HEAD
from PySide2.QtWidgets import QToolButton, QSizePolicy
=======
import sys
from PySide2.QtWidgets import QToolButton, QSizePolicy, QApplication
>>>>>>> d64e29ee0441510161167880cc6dc6837766cf38
from PySide2.QtCore import QSize


class Button(QToolButton):
    def __init__(self, text):
        super(Button, self).__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = QToolButton.sizeHint(self)
        width = size.height() + 20
        height = max(size.width(), size.height())
        hint = QSize(width, height)
        print(hint)
        return hint
<<<<<<< HEAD
=======


if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = Button('test')
    b.sizeHint()
    b.show()
>>>>>>> d64e29ee0441510161167880cc6dc6837766cf38
