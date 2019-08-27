import sys
from math import sqrt
from PySide2.QtWidgets import (QWidget, QGridLayout, QApplication,
                               QLineEdit, QLayout)
from PySide2.QtCore import Slot, Qt
from button import Button


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.sum_in_memory = 0
        self.sum_so_far = 0.0
        self.factor_so_far = 0.0
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
        self.point_button = self.create_button('.',
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
        self.root_button = self.create_button('\u221a',
                                              self.unary_operator_clicked)
        self.square_button = self.create_button('x\u00b2',
                                                self.unary_operator_clicked)
        self.reciproce_button = self.create_button('x\u207b\u2071',
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

        # put the buttons into the setLayout
        self.layout.addWidget(self.display, 0, 0, 1, 6)
        self.layout.addWidget(self.back_button, 1, 0, 1, 2)
        self.layout.addWidget(self.clear_button, 1, 2, 1, 2)
        self.layout.addWidget(self.clear_all_button, 1, 4, 1, 2)

        for i in range(len(self.num_buttons)):
            if i > 0:
                row = int(((9-i)) / 3) + 2
                col = ((i - 1) % 3) + 1
                self.layout.addWidget(self.num_buttons[i], row, col)
            else:
                self.layout.addWidget(self.num_buttons[0], 5, 2)

        self.layout.addWidget(self.memory_clear, 2, 0)
        self.layout.addWidget(self.memory_save, 3, 0)
        self.layout.addWidget(self.memory_read, 4, 0)
        self.layout.addWidget(self.memory_add, 5, 0)
        self.layout.addWidget(self.divide_button, 2, 4)
        self.layout.addWidget(self.multiply_button, 3, 4)
        self.layout.addWidget(self.minus_button, 4, 4)
        self.layout.addWidget(self.plus_button, 5, 4)
        self.layout.addWidget(self.root_button, 2, 5)
        self.layout.addWidget(self.square_button, 3, 5)
        self.layout.addWidget(self.reciproce_button, 4, 5)
        self.layout.addWidget(self.equal_button, 5, 5)
        self.layout.addWidget(self.sign_button, 5, 1)
        self.layout.addWidget(self.point_button, 5, 3)

    @Slot()
    def digit_clicked(self):
        number = int(self.sender().text())
        # print(self.sender(), self.sender.text())
        if number == 0 and self.display.text() == 0:
            return
        if self.waiting_for_operand:
            self.display.clear()
            self.waiting_for_operand = False
        self.display.setText(self.display.text() + str(number))

    @Slot()
    def additive_clicked(self):
        text = self.display.text()
        if text[-1].isdigit():
            clicked_operator = self.sender().text()
            operand = float(text)
            if self.pending_multiplicative_operator != '':
                if not self.calculate(operand,
                                      self.pending_multiplicative_operator):
                    self.abort_operation('zero_div')
                    return
                self.display.setText(str(self.factor_so_far))
                operand = self.factor_so_far
                self.factor_so_far = 0.0
                self.pending_multiplicative_operator = ''
            if self.pending_additive_operator != '':
                if not self.calculate(operand,
                                      self.pending_additive_operator):
                    self.abort_operation('zero_div')
                    return
                self.display.setText(str(self.sum_so_far))
            else:
                self.sum_so_far = operand
            self.pending_additive_operator = clicked_operator
            self.waiting_for_operand = True
        else:
            self.clear_all()

    @Slot()
    def unary_operator_clicked(self):
        text = self.display.text()
        if text[-1].isdigit():
            button = self.sender()
            operator = button.text()
            operand = float(text)
            result = 0.0
            if operator == '\u221a':
                if operand < 0:
                    self.abort_operation('sqrt')
                else:
                    result = sqrt(operand)
                    self.display.setText(str(result))
            if operator == 'x\u207b\u2071':
                if operand == 0:
                    self.abort_operation('zero_div')
                else:
                    result = float(1 / operand)
                    self.display.setText(str(result))
            if operator == 'x\u00b2':
                result = operand**2
                self.display.setText(str(result))
            self.waiting_for_operand = True
        else:
            self.clear_all()

    @Slot()
    def multiplicative_clicked(self):
        text = self.display.text()
        if text[-1].isdigit():
            clicked_operator = self.sender().text()
            operand = float(text)
            if self.pending_multiplicative_operator != '':
                if not self.calculate(operand,
                                      self.pending_multiplicative_operator):
                    self.abort_operation('zero_div')
                    return
                self.display.setText(str(self.factor_so_far))
            else:
                self.factor_so_far = operand
            self.pending_multiplicative_operator = clicked_operator
            self.waiting_for_operand = True
        else:
            self.clear_all()

    @Slot()
    def equal_clicked(self):
        text = self.display.text()
        if text[-1].isdigit():
            operand = float(text)
            if self.pending_multiplicative_operator != '':
                if not self.calculate(operand,
                                      self.pending_multiplicative_operator):
                    self.abort_operation('zero_div')
                    return
                operand = self.factor_so_far
                self.factor_so_far = 0.0
                self.pending_multiplicative_operator = ''
            if self.pending_additive_operator != '':
                if not self.calculate(operand,
                                      self.pending_additive_operator):
                    self.abort_operation('zero_div')
                    return
                self.pending_additive_operator = ''
            else:
                self.sum_so_far = operand
            self.display.setText(str(self.sum_so_far))
            self.sum_so_far = 0.0
            self.waiting_for_operand = True
        else:
            self.clear_all()

    @Slot()
    def point_clicked(self):
        if self.waiting_for_operand:
            self.display.setText('0')
        if '.' not in self.display.text():
            self.display.setText(self.display.text() + '.')
            self.waiting_for_operand = False

    @Slot()
    def change_sign_clicked(self):
        operand = self.display.text()
        if '-' not in operand:
            self.display.setText('-' + operand)
        else:
            self.display.setText(operand[1:])

    @Slot()
    def backspace_clicked(self):
        if self.waiting_for_operand:
            return
        text = self.display.text()[:len(self.display.text()) - 1]
        if text == '':
            self.display.setText('0')
            self.waiting_for_operand = True
        else:
            self.display.setText(text)

    @Slot()
    def clear(self):
        if self.waiting_for_operand:
            return
        self.display.setText('0')
        self.waiting_for_operand = True

    @Slot()
    def clear_all(self):
        self.display.setText('0')
        self.waiting_for_operand = True
        self.sum_so_far = 0
        self.factor_so_far = 0
        self.pending_additive_operator = ''
        self.pending_multiplicative_operator = ''

    @Slot()
    def clear_memory(self):
        self.sum_in_memory = 0

    @Slot()
    def read_memory(self):
        self.waiting_for_operand = True
        self.display.setText(str(self.sum_in_memory))

    @Slot()
    def set_memory(self):
        self.equal_clicked()
        self.sum_in_memory = float(self.display.text())

    @Slot()
    def add_to_memory(self):
        self.equal_clicked()
        self.sum_in_memory += float(self.display.text())

    def create_button(self, text, slot):
        self.new_button = Button(text)
        self.new_button.clicked.connect(slot)
        return self.new_button

    def abort_operation(self, err=None):
        self.clear_all()
        if err is None:
            self.display.setText('Error!')
        if err == 'sqrt':
            self.display.setText('Undefined!')
        if err == 'zero_div':
            self.display.setText('Zero division')

    # calculates a binary operation returns True if possible else False
    def calculate(self, right_operand, pending_operator):
        if pending_operator == '+':
            self.sum_so_far += right_operand
        if pending_operator == '-':
            self.sum_so_far -= right_operand
        if pending_operator == 'x':
            self.factor_so_far *= right_operand
        if pending_operator == '/':
            if right_operand == 0:
                return False
            self.factor_so_far /= right_operand
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Calculator()
    t.show()
    sys.exit(app.exec_())
