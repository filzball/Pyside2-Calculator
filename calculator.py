'''This module computes an equation that should be given in list form.'''

import math


class Calculator:                   # example: ['2', 'x', '6']
    def __init__(self):
        self.operators = ['+', '-', 'x', '/', '^', 'sqrt',
                          '%', '(', ')', 'Pi', 'e']

    def calculate(self, equation):
        self.equation = equation
        print(self.equation)
        if self.equation == []:
            return None

        if len(self.equation) == 1:
            if self.equation[0] not in self.operators:
                return self.equation[0]
            if 'e' in self.equation:
                return str(math.e)
            if 'Pi' in self.equation:
                return str(math.pi)

        
if __name__ == '__main__':
    c = Calculator()
