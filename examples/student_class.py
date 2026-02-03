"""
Student Class Example
Ví dụ về lớp Sinh viên
"""

class Student:
    """Lớp đại diện cho sinh viên / Class representing a student"""
    
    def __init__(self, name, student_id, age):
        """
        Khởi tạo sinh viên / Initialize student
        
        Args:
            name (str): Tên sinh viên / Student name
            student_id (str): Mã sinh viên / Student ID
            age (int): Tuổi / Age
        """
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        """Thêm điểm / Add grade"""
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print(f"Điểm không hợp lệ: {grade} / Invalid grade: {grade}")
    
    def get_average(self):
        """Tính điểm trung bình / Calculate average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        """Hiển thị thông tin sinh viên / Display student information"""
        print(f"\n{'='*50}")
        print(f"Tên / Name: {self.name}")
        print(f"Mã SV / Student ID: {self.student_id}")
        print(f"Tuổi / Age: {self.age}")
        print(f"Điểm / Grades: {self.grades}")
        print(f"Điểm TB / Average: {self.get_average():.2f}")
        print(f"{'='*50}")

def main():
    """Main function"""
    # Tạo sinh viên / Create students
    student1 = Student("Nguyễn Văn A", "SV001", 20)
    student2 = Student("Trần Thị B", "SV002", 21)
    
    # Thêm điểm / Add grades
    student1.add_grade(8.5)
    student1.add_grade(9.0)
    student1.add_grade(7.5)
    
    student2.add_grade(9.5)
    student2.add_grade(8.0)
    student2.add_grade(9.0)
    
    # Hiển thị thông tin / Display information
    student1.display_info()
    student2.display_info()

if __name__ == "__main__":
    main()
