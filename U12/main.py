"""
Person nomli class yarating va undan Student va Teacher nomli class larni voris qilib oling.
Quyidagi methodani yarating

"""

#code

class Person:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address

    def getName(self):
        return f"Name:{self.name}"

    def getAddress(self):
        return f"Address:{self.name}"

    def setAddress(self,new_address : str):
        self.address = new_address

    def toSrting(self):
        return f"{self.name}({self.address})"
    

class Student(Person):
    def __init__(self, name, address) -> None:
        super().__init__(name, address)
        self.numCourses = 0
        self.courses = []
        self.grades = []

    def toSrting(self):
        return f"Student:{self.name}({self.address})"

    def addCourseGrade(self,course : str,grade : int):
        self.courses.append(course)
        self.grades.append(grade)

    def printGrades(self):
        for grade in self.grades:
            print(grade)

    def getAverageGrade(self):
        lenth = len(self.grades)
        total = sum(self.grades)
        average = total / lenth
        return average 
    

class Teacher(Person):
    def __init__(self, name, address) -> None:
        super().__init__(name, address)
        self.numCourses = 0
        self.courses = []
    
    def addCourse(self,course):
        if course not in self.courses:
            self.courses.append(course)
            return True
        else:
            print("Bu kurs mavjud")
            return False
        
    def removeCourse(self,course):
        if course not in self.courses:
            print("Yoq kursni o`chirib tashayolmaysiz")
            return False
        else:
            self.courses.remove(course)
            return True
        
    def toSrting(self):
        return f"Teacher:{self.name}({self.address})"
print()
    

student1 =Student("ali","olmazor")
teacher1 =Teacher("ali","olmazor")

teacher1.addCourse("math")
teacher1.addCourse("science")
teacher1.removeCourse("history")

print(student1.toSrting())
print()