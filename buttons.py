import sys
from PySide2.QtWidgets import (QWidget, QPushButton, QGridLayout, QApplication,
                               QVBoxLayout, QLabel, QHBoxLayout)
from PySide2.QtCore import Slot
from calculator import Calculator


class CalcWidget(QWidget):
    def __init__(self):
        super(CalcWidget, self).__init__()

        # vertical layout
        vl = QVBoxLayout()
        vl.addStretch(1)
        self.label = QLabel('', self)
        vl.addWidget(self.label)
        self.setLayout(vl)

        # button layout with shortcuts
        self.buttons = ['(', ')', '^', 'sqrt',
                        '1', '2', '3', '/',
                        '4', '5', '6', 'x',
                        '7', '8', '9', '-',
                        'Pi', '0', 'e', '+']
        grid = QGridLayout()
        # grid.setVerticalSpacing(5)
        coords = [(x, y) for x in range(5) for y in range(4)]
        for name, coord in zip(self.buttons, coords):
            butt = QPushButton(name)
            butt.setShortcut(name)
            butt.clicked.connect(self.set_label_text)
            butt.setMinimumWidth(25)
            grid.addWidget(butt, *coord)

        # equals and C button
        hl = QHBoxLayout()

        eq = QPushButton('=')
        eq.setShortcut('Return')

        CButt = QPushButton('C')
        CButt.setShortcut('c')

        hl.addWidget(eq)
        hl.addWidget(CButt)
        eq.clicked.connect(self.compute)
        CButt.clicked.connect(self.flush_label)

        vl.addLayout(grid)
        vl.addLayout(hl)

    @Slot()
    def set_label_text(self):
        char = self.sender().text()
        if char.isdigit():
            self.label.setText(self.label.text() + char)
            # print(char)
        else:
            self.label.setText(self.label.text() + ' ' + char + ' ')

    @Slot()
    def compute(self):
        term = self.label.text()
        operands = term.split(' ')
        while '' in operands:
            operands.remove('')
        # print(operands)
        self.calc = Calculator()
        result = self.calc.calculate(operands)
        # print(result)
        self.label.setText(result)
        # self.label.setText('')

    @Slot()
    def flush_label(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CalcWidget()
    w.show()
    sys.exit(app.exec_())
