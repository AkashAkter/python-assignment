def is_valid_expression(expression):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    allowed_chars = set('()[]{}+-*/%0123456789')
    
    # Check for invalid characters
    for char in expression:
        if char not in allowed_chars:
            return False
    
    # Check bracket matching
    for char in expression:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    return len(stack) == 0

def calculate_expression(expression):
    try:
        # Replace brackets with parentheses for eval
        expression = expression.replace('[', '(').replace(']', ')')
        expression = expression.replace('{', '(').replace('}', ')')
        return eval(expression)
    except:
        return None

def calculator():
    while True:
        print("\nCalculator")
        expression = input("Enter an expression (or 'quit' to exit): ").strip()
        
        if expression.lower() == 'quit':
            break
        
        if not is_valid_expression(expression):
            print("Invalid expression! Please use only digits, +-*/%, and matching brackets ()[]{}")
            continue
        
        result = calculate_expression(expression)
        if result is not None:
            print(f"Result: {result}")
        else:
            print("Error in calculation. Please check your expression.")
        
        continue_calc = input("Continue? (y/n): ").strip().lower()
        if continue_calc != 'y':
            break

if __name__ == "__main__":
    calculator()