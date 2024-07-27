from sympy import symbols, Eq, solve, sympify
class EquationSolver:
    def __init__(self):
        self.x = symbols('x')

    def parse_equation(self, equation_str):
        if '=' in equation_str:
            lhs, rhs = equation_str.split('=')
            lhs = self._format_expression(lhs)
            rhs = self._format_expression(rhs)
            return Eq(sympify(lhs), sympify(rhs))
        else:
            raise ValueError("Equation must contain an '=' sign.")

    def solve_equation(self, equation_str):
        equation = self.parse_equation(equation_str)
        solution = solve(equation, self.x)
        return solution

    def _format_expression(self, expression):
        # Replace '^' with '**' for exponentiation
        return expression.replace('^', '**')
