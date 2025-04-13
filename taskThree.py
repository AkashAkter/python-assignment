class Calculator:
    def __init__(self):
        self.allowed_chars = set('0123456789+-*/%()[]{} ')
        self.bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    
    def is_valid_expression(self, expr):
        """Verify that the expression has balanced brackets and only permitted characters"""
        stack = []
        
        for char in expr:
            if char not in self.allowed_chars:
                return False
            
            if char in self.bracket_pairs:
                stack.append(self.bracket_pairs[char])
            elif char in self.bracket_pairs.values():
                if not stack or char != stack.pop():
                    return False
        
        return not stack 
    
    def evaluate_expression(self, expr):
        """After validation, safely assess the expression"""
        try:
          
            expr = expr.replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')
            result = eval(expr)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except:
            return "Error: Invalid expression"
    
    def display_welcome_message(self):
        """Display the welcome message and instructions"""
        print("Here is the Python Calculator.")
        print("Allowed characters: digits, +, -, *, /, %, (, ), [, ], {, }")
        print("Type 'end' to exit the program.\n")
    
    def get_user_input(self):
        """Get and validate user input"""
        while True:
            expression = input("Enter a mathematical expression: ").strip()
            
            if expression.lower() == 'end':
                return None
            
            if not expression:
                print("Error: Empty input. Please enter a valid expression.")
                continue
            
            if not self.is_valid_expression(expression):
                print("Error: Invalid input. Only numbers and the permitted operators/brackets should be used.")
                print("Also check that your brackets are properly balanced.")
                continue
            
            return expression
    
    def run(self):
        """Main method to run the calculator"""
        self.display_welcome_message()
        
        while True:
            expression = self.get_user_input()
            
            if expression is None:
                print("Goodbye!")
                break
            
            result = self.evaluate_expression(expression)
            
            if isinstance(result, str) and result.startswith("Error"):
                print(result)
            else:
                print(f"Result: {result}")
            
          
            while True:
                choice = input("\nCalculate another expression? (yes/no): ").strip().lower()
                if choice in ('yes', 'y'):
                    print()  
                    break
                elif choice in ('no', 'n'):
                    print("Thank you for using the calculator.")
                    return
                else:
                    print("Please enter 'yes' or 'no'.")


# Main program
if __name__ == "__main__":
    app = Calculator()
    app.run()