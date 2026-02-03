"""
Simple Calculator
Máy tính đơn giản
"""

def add(a, b):
    """Cộng hai số / Add two numbers"""
    return a + b

def subtract(a, b):
    """Trừ hai số / Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Nhân hai số / Multiply two numbers"""
    return a * b

def divide(a, b):
    """Chia hai số / Divide two numbers"""
    if b == 0:
        return "Không thể chia cho 0 / Cannot divide by zero"
    return a / b

def main():
    """Main function"""
    print("=== Máy tính đơn giản / Simple Calculator ===\n")
    
    # Ví dụ sử dụng / Usage examples
    num1 = 10
    num2 = 5
    
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
    
    # Thử chia cho 0 / Try division by zero
    print(f"\n{num1} / 0 = {divide(num1, 0)}")

if __name__ == "__main__":
    main()
