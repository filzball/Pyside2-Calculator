import sys
from PySide2.QtWidgets import (QWidget, QGridLayout, QApplication,
                               QLineEdit)
from PySide2.QtCore import Slot, Qt


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.sum_in_memory = 0
        self.sum_so_far = 0
        self.factor_so_far = 0
        self.pending_additive_operator = ''  # last + or - operator
        self.pending_multiplicative_operator = ''  # last x or / operator
        self.waiting_for_operand = True

        self.num_buttons = [i for i in range(10)]

        # create the display
        self.display = QLineEdit('0', self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.layout = QGridLayout()

    @Slot()
    def digit_clicked(self):
        pass

    @Slot()
    def additive_operator_clicked(self):
        pass

    @Slot()
    def unary_operator_clicked(self):
        pass

    @Slot()
    def multiplicative_operator_clicked(self):
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
        pass

# Button *Calculator::createButton(const QString &text, const char *member)
# {
#     Button *button = new Button(text);
#     connect(button, SIGNAL(clicked()), this, member);
#     return button;
# }

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
