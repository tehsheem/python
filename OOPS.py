# class Student:
#     name = "Nia"
    
# s1 = Student()
# print(s1.name)

# class Student:
#     name = "Kakashi"
# s1 = Student()
# print(s1.name)

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
# s1 = Student("Karan")
# print(s1.name)

# class Student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in the database")
# s2 = Student("itachi", 56)
# print(s2.name, s2.marks)

# s3 = Student("Sasuke", 89)
# print(s3.name, s3.marks)

# class Student():
#     collegename = "ABC"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in the database")
# s1 = Student("Kakashi" , 89)
# print(s1.name, s1.marks,)
# print(s1.collegename)

# s2 = Student("Itachi", 89)
# print(s2.name, s2.marks)
# print(Student.collegename)

class Student:
    
    collegename = "COLLEGE ABC"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    print("adding new stuent into the database")
s1 = Student("Kakashi", 87)
print(s1.name, s1.marks)
print(Student.collegename)

s2 = Student("Sasuke", 89)
print(s2.name, s2.marks)
print(Student.collegename)