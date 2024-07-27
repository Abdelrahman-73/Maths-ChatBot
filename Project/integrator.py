from sympy import symbols, integrate
class Integrator:
    def __init__(self):
        self.x = symbols('x')

    def definite_integral(self, func_str, lower_limit, upper_limit):
        func = self._format_expression(func_str)
        result = integrate(func, (self.x, lower_limit, upper_limit))
        steps = f"Integrate {func} from {lower_limit} to {upper_limit}"
        return result, steps

    def indefinite_integral(self, func_str):
        func = self._format_expression(func_str)
        result = integrate(func, self.x)
        steps = f"Integrate {func} indefinitely"
        return result, steps

    def format_steps(self, steps):
        return steps

    def _format_expression(self, expression):
        # Replace '^' with '**' for exponentiation
        return expression.replace('^', '**')
