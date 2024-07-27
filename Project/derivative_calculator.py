from sympy import symbols, diff
class DerivativeCalculator:
    def __init__(self):
        self.x = symbols('x')

    def compute_derivative(self, func_str):
        func = self._format_expression(func_str)
        derivative = diff(func, self.x)
        return derivative

    def _format_expression(self, expression):
        # Replace '^' with '**' for exponentiation
        return expression.replace('^', '**')
