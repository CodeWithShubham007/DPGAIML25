# class Students:
#     # name: print("Hello")
#     def __init__(self):
#         # print("Hello Duniya!!!")
#         print(self)


# stu1 = Students()  # Creating Object
# stu2 = Students()  # Creating Object
# print(stu1)
# print(stu2)


# class calculator:
#     def add(self, num1, num2):
#         return num1+num2
#     def sub(self, num1, num2):
#         return num1 - num2
#     def multi(self, num1, num2, num3):
#         return num1 * num2 * num3
#     def divide(self, num1, num2):
#         return num2/num1

# cal1 = calculator();
# print(cal1.add(5, 10))
# cal2 = calculator()
# print(cal2.multi(3,4,5))

# Q. Create a student class that takes the name & marks of 5 subjects as arguments 
# in the constructor. then create a method to print the average.

# class Students:
#     def get_avgMarks(self, name, marks):
#         sum = 0;
#         for val in marks:
#             sum += val
#         return f"Student name: {name} & Average Marks: {(sum)/5}"

# stu1 = Students();
# print(stu1.get_avgMarks("Abc", [90, 80, 98, 67, 55]))

# class StudentData:
#     def get_Avg(self, name, sub1, sub2, sub3, sub4, sub5):
#         return f"{name} {(sub1+sub2+sub3+sub4+sub5)/5}"

# stud1 = StudentData();
# print(stud1.get_Avg("Abc", 90, 80, 98, 67, 55))

# class Car:
#     def get_carDetails(self, name, model):
#         self.vName = name
#         self.vModel = model
#         print(self.vName, self.vModel)

# car1 = Car();
# car1.get_carDetails("Hero", 2025)

# inheritance
class College:
    def __init__(self, name):
        self.name = name
    
class Student1(College): 
    def getDetails(self):
        print(f"{self.name} is our students")

stu1 = Student1("Abc");

stu1.getDetails()