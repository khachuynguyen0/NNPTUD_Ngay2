"""
Exercise 1: Basic Python Operations
Bài tập 1: Các thao tác Python cơ bản

TODO: Hoàn thành các hàm bên dưới / Complete the functions below
"""

def calculate_sum(numbers):
    """
    Tính tổng các số trong danh sách
    Calculate the sum of numbers in a list
    
    Args:
        numbers (list): Danh sách số / List of numbers
    
    Returns:
        int/float: Tổng các số / Sum of numbers
    
    Example:
        >>> calculate_sum([1, 2, 3, 4, 5])
        15
    """
    # TODO: Viết code ở đây / Write your code here
    pass

def find_max(numbers):
    """
    Tìm số lớn nhất trong danh sách
    Find the maximum number in a list
    
    Args:
        numbers (list): Danh sách số / List of numbers
    
    Returns:
        int/float: Số lớn nhất / Maximum number
    
    Example:
        >>> find_max([1, 5, 3, 9, 2])
        9
    """
    # TODO: Viết code ở đây / Write your code here
    pass

def is_even(number):
    """
    Kiểm tra số chẵn
    Check if a number is even
    
    Args:
        number (int): Số cần kiểm tra / Number to check
    
    Returns:
        bool: True nếu chẵn, False nếu lẻ / True if even, False if odd
    
    Example:
        >>> is_even(4)
        True
        >>> is_even(5)
        False
    """
    # TODO: Viết code ở đây / Write your code here
    pass

def reverse_string(text):
    """
    Đảo ngược chuỗi
    Reverse a string
    
    Args:
        text (str): Chuỗi cần đảo ngược / String to reverse
    
    Returns:
        str: Chuỗi đã đảo ngược / Reversed string
    
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    # TODO: Viết code ở đây / Write your code here
    pass

def main():
    """Test your functions / Kiểm tra các hàm của bạn"""
    print("=== Bài tập 1: Thử nghiệm / Exercise 1: Testing ===\n")
    
    # Test calculate_sum
    test_numbers = [1, 2, 3, 4, 5]
    print(f"Tổng của {test_numbers}: {calculate_sum(test_numbers)}")
    
    # Test find_max
    print(f"Số lớn nhất trong {test_numbers}: {find_max(test_numbers)}")
    
    # Test is_even
    print(f"Số 4 có phải số chẵn? {is_even(4)}")
    print(f"Số 7 có phải số chẵn? {is_even(7)}")
    
    # Test reverse_string
    test_string = "hello"
    print(f"Đảo ngược '{test_string}': {reverse_string(test_string)}")

if __name__ == "__main__":
    main()
