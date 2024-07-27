import tkinter as tk
from tkinter import ttk
from equation_solver import EquationSolver
from derivative_calculator import DerivativeCalculator
from integrator import Integrator
import random

class MathChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Chatbot")

        self.equation_solver = EquationSolver()
        self.derivative_calculator = DerivativeCalculator()
        self.integrator = Integrator()
        self.chat_history = []

        self.create_widgets()
        self.display_message("Hello! How can I help you?")

    def create_widgets(self):
        # Chat History Section
        self.chat_history_text = tk.Text(self.root, height=20, width=80)
        self.chat_history_text.pack(pady=5)
        self.chat_history_text.configure(state=tk.DISABLED)

        # Input Section
        self.input_label = tk.Label(self.root, text="Enter your query:")
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack(pady=5)

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        self.solve_button.pack(pady=5)

    def solve(self):
        user_input = self.input_entry.get().strip()
        self.display_message(user_input, is_user=True)

        if not user_input:
            # Display a random response if input is empty
            random_response = self.generate_random_response()
            self.display_message(random_response)
        else:
            result = self.process_input(user_input)
            self.display_message(result)

        self.input_entry.delete(0, tk.END)

    def display_message(self, message, is_user=False):
        self.chat_history_text.configure(state=tk.NORMAL)
        if is_user:
            self.chat_history_text.insert(tk.END, "You: " + message + "\n\n")
        else:
            self.chat_history_text.insert(tk.END, "Bot: " + message + "\n\n")
        self.chat_history_text.configure(state=tk.DISABLED)
        self.chat_history_text.see(tk.END)

    def process_input(self, user_input):
        user_input = user_input.lower()  # Convert to lowercase for easier processing

        if "how are you" in user_input:
            return "I'm just a computer program, so I don't have feelings, but thanks for asking!"
        elif "hello" in user_input or "hi" in user_input:
            return "Hello! How can I assist you today?"
        else:
            try:
                user_input = user_input.replace(' ', '')  # Remove spaces for simplicity

                if "canyousolve" in user_input:
                    equation_str = user_input.replace("canyousolve", "").replace("?", "").strip()
                    if '=' not in equation_str:
                        equation_str += '=0'  # Assume equation is set to 0 if no '=' is provided
                    solution = self.equation_solver.solve_equation(equation_str)
                    return f"Solutions: {solution}"
                elif "canyoudiff" in user_input:
                    func_str = user_input.replace("canyoudiff", "").replace("?", "").strip()
                    derivative = self.derivative_calculator.compute_derivative(func_str)
                    return f"Derivative: {self._format_output(derivative)}"
                elif "canyouint" in user_input:
                    func_str = user_input.replace("canyouint", "").replace("?", "").strip()
                    if "from" in user_input and "to" in user_input:
                        parts = user_input.split()
                        lower_limit = float(parts[-3])
                        upper_limit = float(parts[-1])
                        result, steps = self.integrator.definite_integral(func_str, lower_limit, upper_limit)
                        formatted_steps = self.integrator.format_steps(steps)
                        return f"Integral from {lower_limit} to {upper_limit}: {self._format_output(result)}\nSteps: {formatted_steps}"
                    else:
                        result, steps = self.integrator.indefinite_integral(func_str)
                        formatted_steps = self.integrator.format_steps(steps)
                        return f"Integral: {self._format_output(result)}\nSteps: {formatted_steps}"
                elif "solve" in user_input:
                    equation_str = user_input.replace("solve", "").strip()
                    if '=' not in equation_str:
                        equation_str += '=0'  # Assume equation is set to 0 if no '=' is provided
                    solution = self.equation_solver.solve_equation(equation_str)
                    return f"Solutions: {solution}"
                elif "diff" in user_input:
                    func_str = user_input.replace("diff", "").strip()
                    derivative = self.derivative_calculator.compute_derivative(func_str)
                    return f"Derivative: {self._format_output(derivative)}"
                elif "int" in user_input:
                    func_str = user_input.replace("int", "").strip()
                    if "from" in user_input and "to" in user_input:
                        parts = user_input.split()
                        lower_limit = float(parts[-3])
                        upper_limit = float(parts[-1])
                        result, steps = self.integrator.definite_integral(func_str, lower_limit, upper_limit)
                        formatted_steps = self.integrator.format_steps(steps)
                        return f"Integral from {lower_limit} to {upper_limit}: {self._format_output(result)}\nSteps: {formatted_steps}"
                    else:
                        result, steps = self.integrator.indefinite_integral(func_str)
                        formatted_steps = self.integrator.format_steps(steps)
                        return f"Integral: {self._format_output(result)}\nSteps: {formatted_steps}"
                else:
                    return self.generate_random_response()
            except Exception as e:
                return f"An error occurred: {e}"

    def generate_random_response(self):
        responses = [
            "I'm not sure I understand. Can you please rephrase that?",
            "Hmm... Let me think about that for a moment.",
            "Interesting question! Let me find the answer for you.",
            "I'm still learning! Could you ask me something else?",
            "I'm not programmed for that query. Can you try something different?"
        ]
        return random.choice(responses)

    def _format_output(self, output):
        output_str = str(output)
        output_str = output_str.replace('**', '^')
        return output_str


if __name__ == "__main__":
    root = tk.Tk()
    app = MathChatbotGUI(root)
    root.mainloop()
