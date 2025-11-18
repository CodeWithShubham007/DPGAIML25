# str = "Hello My Name is Shubham, i am a web developer, working in a product based company"

# str1 = "company name is ABC"

# print(f"{str}, {str1}")
# print(str1 * 3)
# print(str[0])

# print(len(str))

# print("p" in str)
listData = [34,65,66,34, 89,75,34,22,90,12,45]
# Q1. separate elements of list - even and odd

# evenData = []
# oddData = []

# for i in listData:
#     if i % 2 == 0:
#         evenData.append(i)
#         # print(i, "is even")
#     else:
#         oddData.append(i)

# print("Even List:", evenData)
# print("Odd List:", oddData)
# evenList = []

# for i in listData:
#     if i % 2 == 0:
#         evenList.append(i)
#     else:
#         oddList.append(i)

# print("Even List:", evenList)
# print("Odd List:", oddList)

# Q2. write python program, where combine to list and it should be in sorted order.












# list1 = [2,4,6,8,10]
# list2 = [1,3,5,7,9]
# list1 = [2,4,6,8,10]
# list2 = [1,3,5,7,9]
# combinedList = list1 + list2
# combinedList.sort()
# print("Combined Sorted List:", combinedList)
# print("Combined Sorted List:", list1 + list2)


# abc = {11,2,3,4,5,2,3,2,4, "Hello", "hello", "Hello"}
# print(abc)


# OOPs

# class Students: # create class
#     name = "Shubham"  # create attribute

# Stu1 = Students()  # create object
# print(Stu1)  # access attribute using object

# class Calculator:
#     num1 = 10
#     num2 = 5

#     def add(self):
#         return self.num1 + self.num2

#     def sub(self):
#         return self.num1 - self.num2

#     def mul(self):
#         return self.num1 * self.num2

#     def div(self):
#         return self.num1 / self.num2

# calc = Calculator()
# print("Addition:", calc.add())

# Note - Class & Instance Attributes
# Class Attribute - Attribute which is shared by all the objects of the class

# Create a student class that takes the name & marks of 3 subjects as arguments in constructor. then create a method to print the average.
# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avgMarks(self):
#         sum = 0;
#         for cal in self.marks:
#             sum += cal;
#         return sum/3;
    
#     @staticmethod
#     def age():
#         age: 20

# stu1 = Students("Shubham", [100, 100, 100])
# print(stu1.get_avgMarks())
# print()


# File
# f = open("D:\\College Doc\\Shubham.txt", "w");
# f.write("Hello Duniya");
# f.close()


# f = open("D:\\College Doc\\Shubham.txt", "a");
# f.write("\nHello Ji!!!");
# f.close()

# f = open("D:\\College Doc\\Shubham.txt", "r");
# fileS=f.read()
# print(fileS)
# f.close()

# f = open("D:\\College Doc\\Shubham.txt", "r");
# # fileS=f.read()
# for words in f:
#     count = words.split(" ")
#     print(len(count))
# f.close()