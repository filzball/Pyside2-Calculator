from PySide2.QtWidgets import QToolButton, QSizePolicy
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
        # print(hint)
        return hint
