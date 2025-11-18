# class Student:
#     def __init__(self):
#         self.__marks = 90  # private variable

#     def get_marks(self):
#         return self.__marks

# s = Student()
# print(s.get_marks())

# Encapsulation Ex - 2
# class Employee:
#     def __init__(self, name, sal):
#         self.name = name  # public attributes
#         self.__sal = sal  ## private Attributes

#     def get_sal(self):
#         return self.__sal

#     def set_sal(self, amount):
#         self.__sal = amount

# #object creation
# Emp1 = Employee("Abc", 7000);
# Emp1.set_sal(10000)
# print(Emp1.get_sal())
# print(Emp1.name)


# Polymorphism

# print(len(["Python"|)
# print(len([1,2,3,4]))
# print(len("Python"));


# class Dog:
#     def speak(self):
#         print("Woof!!!!")

# class Cat:
#     def speak(self):
#         print("Meow!!!")

# animals = [Dog(), Cat()]

# for i in animals:
#     i.speak()

# Write Mode
# f = open("D:\\Books\\DSA\\demo.txt", 'w');
# f.write("This is my JavaScript!!!")
# f.close()

# # Append Mode
# f =open("D:\\Books\\DSA\\demo.txt", 'a');
# f.write("\nThis is my C++!!!")
# f.close()

# Read Mode
# f = open("D:\\Books\\DSA\\demo.txt", 'r');
# content = f.read();
# print(len(content))
# f.close()

# max in 3 number
num1 = int(input("Enter Your 1st Number: "));
num2 = int(input("Enter Your 2nd Number: "));
num3 = int(input("Enter Your 3rd Number: "));

def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(find_max(num1, num2, num3))