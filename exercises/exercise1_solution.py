"""
Exercise 1 Solutions
Đáp án Bài tập 1
"""

def calculate_sum(numbers):
    """
    Tính tổng các số trong danh sách
    Calculate the sum of numbers in a list
    """
    return sum(numbers)

def find_max(numbers):
    """
    Tìm số lớn nhất trong danh sách
    Find the maximum number in a list
    """
    return max(numbers)

def is_even(number):
    """
    Kiểm tra số chẵn
    Check if a number is even
    """
    return number % 2 == 0

def reverse_string(text):
    """
    Đảo ngược chuỗi
    Reverse a string
    """
    return text[::-1]

def main():
    """Test the solutions / Kiểm tra đáp án"""
    print("=== Đáp án Bài tập 1 / Exercise 1 Solutions ===\n")
    
    # Test calculate_sum
    test_numbers = [1, 2, 3, 4, 5]
    print(f"Tổng của {test_numbers}: {calculate_sum(test_numbers)}")
    print(f"Sum of {test_numbers}: {calculate_sum(test_numbers)}")
    
    # Test find_max
    print(f"\nSố lớn nhất trong {test_numbers}: {find_max(test_numbers)}")
    print(f"Maximum in {test_numbers}: {find_max(test_numbers)}")
    
    # Test is_even
    print(f"\nSố 4 có phải số chẵn? {is_even(4)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Số 7 có phải số chẵn? {is_even(7)}")
    print(f"Is 7 even? {is_even(7)}")
    
    # Test reverse_string
    test_string = "hello"
    print(f"\nĐảo ngược '{test_string}': {reverse_string(test_string)}")
    print(f"Reverse of '{test_string}': {reverse_string(test_string)}")

if __name__ == "__main__":
    main()
