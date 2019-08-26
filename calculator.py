import sys
from PySide2.QtWidgets import (QWidget, QGridLayout, QApplication,
                               QLineEdit, QLayout)
from PySide2.QtCore import Slot, Qt
from button import Button


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.sum_in_memory = 0
        self.sum_so_far = 0
        self.factor_so_far = 0
        self.pending_additive_operator = ''  # last + or - operator
        self.pending_multiplicative_operator = ''  # last x or / operator
        self.waiting_for_operand = True

        self.num_buttons = []

        # create the display
        self.display = QLineEdit('0', self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        # create all the buttons
        for i in range(10):
            button = self.create_button(str(i), self.digit_clicked)
            self.num_buttons.append(button)
        self.digit_button = self.create_button('.',
                                               self.point_clicked)
        self.sign_button = self.create_button('\u00b1',
                                              self.change_sign_clicked)
        self.plus_button = self.create_button('+',
                                              self.additive_clicked)
        self.minus_button = self.create_button('-',
                                               self.additive_clicked)
        self.multiply_button = self.create_button('x',
                                                  self.multiplicative_clicked)
        self.divide_button = self.create_button('/',
                                                self.multiplicative_clicked)
        self.root_button = self.create_button('sqrt',
                                              self.unary_operator_clicked)
        self.square_button = self.create_button('x^2',
                                                self.unary_operator_clicked)
        self.reciproce_button = self.create_button('1/x',
                                                   self.unary_operator_clicked)
        self.equal_button = self.create_button('=',
                                               self.equal_clicked)
        self.back_button = self.create_button('\u2190',
                                              self.backspace_clicked)
        self.clear_button = self.create_button('Clear',
                                               self.clear)
        self.clear_all_button = self.create_button('Clear All',
                                                   self.clear_all)
        self.memory_clear = self.create_button('MC',
                                               self.clear_memory)
        self.memory_add = self.create_button('M+',
                                             self.add_to_memory)
        self.memory_read = self.create_button('MR',
                                              self.read_memory)
        self.memory_save = self.create_button('MS',
                                              self.set_memory)
        # create a grid layout
        self.layout = QGridLayout()
        self.layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.layout)

    @Slot()
    def digit_clicked(self):
        pass

    @Slot()
    def additive_clicked(self):
        pass

    @Slot()
    def unary_operator_clicked(self):
        pass

    @Slot()
    def multiplicative_clicked(self):
        pass

    @Slot()
    def equal_clicked(self):
        pass

    @Slot()
    def point_clicked(self):
        pass

    @Slot()
    def change_sign_clicked(self):
        pass

    @Slot()
    def backspace_clicked(self):
        pass

    @Slot()
    def clear(self):
        pass

    @Slot()
    def clear_all(self):
        pass

    @Slot()
    def clear_memory(self):
        pass

    @Slot()
    def read_memory(self):
        pass

    @Slot()
    def set_memory(self):
        pass

    @Slot()
    def add_to_memory(self):
        pass

    def create_button(self, text, slot):
        self.new_button = Button(text)
        self.new_button.clicked.connect(slot)
        return self.new_button

    def abort_operation(self):
        pass

    def calculate(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Calculator()
    t.resize(300, 300)
    t.show()
    sys.exit(app.exec_())
