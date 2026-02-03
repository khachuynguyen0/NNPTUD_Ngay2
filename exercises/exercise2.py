"""
Exercise 2: Working with Classes
Bài tập 2: Làm việc với lớp

TODO: Hoàn thành lớp Book bên dưới / Complete the Book class below
"""

class Book:
    """
    Lớp đại diện cho một cuốn sách
    Class representing a book
    """
    
    def __init__(self, title, author, year, pages):
        """
        Khởi tạo sách / Initialize book
        
        Args:
            title (str): Tên sách / Book title
            author (str): Tác giả / Author
            year (int): Năm xuất bản / Publication year
            pages (int): Số trang / Number of pages
        """
        # TODO: Khởi tạo các thuộc tính / Initialize attributes
        pass
    
    def get_info(self):
        """
        Lấy thông tin sách dưới dạng chuỗi
        Get book information as a string
        
        Returns:
            str: Thông tin sách / Book information
        """
        # TODO: Trả về thông tin sách / Return book information
        pass
    
    def is_classic(self):
        """
        Kiểm tra xem sách có phải là sách cổ điển không (xuất bản trước năm 2000)
        Check if the book is a classic (published before 2000)
        
        Returns:
            bool: True nếu là sách cổ điển / True if classic
        """
        # TODO: Viết code kiểm tra / Write checking code
        pass

class Library:
    """
    Lớp đại diện cho thư viện
    Class representing a library
    """
    
    def __init__(self, name):
        """
        Khởi tạo thư viện / Initialize library
        
        Args:
            name (str): Tên thư viện / Library name
        """
        # TODO: Khởi tạo thuộc tính / Initialize attributes
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """
        Thêm sách vào thư viện
        Add a book to the library
        
        Args:
            book (Book): Sách cần thêm / Book to add
        """
        # TODO: Thêm sách vào danh sách / Add book to list
        pass
    
    def list_books(self):
        """
        Liệt kê tất cả các sách trong thư viện
        List all books in the library
        """
        # TODO: In ra thông tin tất cả các sách / Print all books' information
        pass
    
    def count_classics(self):
        """
        Đếm số lượng sách cổ điển trong thư viện
        Count the number of classic books in the library
        
        Returns:
            int: Số lượng sách cổ điển / Number of classic books
        """
        # TODO: Đếm và trả về số sách cổ điển / Count and return classic books
        pass

def main():
    """Test your classes / Kiểm tra các lớp của bạn"""
    print("=== Bài tập 2: Thử nghiệm / Exercise 2: Testing ===\n")
    
    # Tạo thư viện / Create library
    library = Library("Thư viện NNPTUD")
    
    # Tạo sách / Create books
    book1 = Book("Python Programming", "John Smith", 2020, 350)
    book2 = Book("Classic Literature", "Jane Doe", 1995, 420)
    book3 = Book("Modern Web Development", "Bob Johnson", 2022, 500)
    
    # Thêm sách vào thư viện / Add books to library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Liệt kê sách / List books
    print(f"Thư viện: {library.name}\n")
    library.list_books()
    
    # Đếm sách cổ điển / Count classics
    print(f"\nSố lượng sách cổ điển: {library.count_classics()}")

if __name__ == "__main__":
    main()
