"""
Exercise 2 Solutions
Đáp án Bài tập 2
"""

class Book:
    """
    Lớp đại diện cho một cuốn sách
    Class representing a book
    """
    
    def __init__(self, title, author, year, pages):
        """Khởi tạo sách / Initialize book"""
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    
    def get_info(self):
        """Lấy thông tin sách / Get book information"""
        return f"'{self.title}' by {self.author} ({self.year}) - {self.pages} pages"
    
    def is_classic(self):
        """Kiểm tra sách cổ điển / Check if classic"""
        return self.year < 2000

class Library:
    """
    Lớp đại diện cho thư viện
    Class representing a library
    """
    
    def __init__(self, name):
        """Khởi tạo thư viện / Initialize library"""
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """Thêm sách vào thư viện / Add book to library"""
        self.books.append(book)
        print(f"Đã thêm: {book.get_info()}")
        print(f"Added: {book.get_info()}")
    
    def list_books(self):
        """Liệt kê tất cả các sách / List all books"""
        if not self.books:
            print("Thư viện trống / Library is empty")
            return
        
        print("Danh sách sách / Book list:")
        for i, book in enumerate(self.books, 1):
            classic_mark = " [Cổ điển/Classic]" if book.is_classic() else ""
            print(f"{i}. {book.get_info()}{classic_mark}")
    
    def count_classics(self):
        """Đếm số sách cổ điển / Count classic books"""
        return sum(1 for book in self.books if book.is_classic())

def main():
    """Test the solutions / Kiểm tra đáp án"""
    print("=== Đáp án Bài tập 2 / Exercise 2 Solutions ===\n")
    
    # Tạo thư viện / Create library
    library = Library("Thư viện NNPTUD / NNPTUD Library")
    
    # Tạo sách / Create books
    book1 = Book("Python Programming", "John Smith", 2020, 350)
    book2 = Book("Classic Literature", "Jane Doe", 1995, 420)
    book3 = Book("Modern Web Development", "Bob Johnson", 2022, 500)
    book4 = Book("Old Programming Guide", "Alice Brown", 1998, 280)
    
    # Thêm sách vào thư viện / Add books to library
    print("Thêm sách / Adding books:\n")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    
    # Liệt kê sách / List books
    print(f"\n{'='*60}")
    print(f"Thư viện: {library.name}")
    print(f"{'='*60}\n")
    library.list_books()
    
    # Đếm sách cổ điển / Count classics
    classic_count = library.count_classics()
    print(f"\nSố lượng sách cổ điển: {classic_count}")
    print(f"Number of classic books: {classic_count}")

if __name__ == "__main__":
    main()
