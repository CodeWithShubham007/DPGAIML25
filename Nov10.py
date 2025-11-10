# list = [11, 45, 75, 23, 43, 65];
# 1. find the position of 75
# 2. find the position of 26

# list[i], list[i], list[i]
# num = 75;
# num = int(input("Enter Searching Number: "))
# def searchLinear(list, num):
#     for i in range(len(list)):
#         if list[i] == num:
#             return i;
#         else:
#             print("Not Found...")

# value = searchLinear(list, num);
# print(value)

nums = int(input("Enter Your Number: "))
# Prime Number
def findPrime(nums):
    count = 0;
    for i in range(1, nums + 1):
        if nums % i == 0:
            count = count + 1;
    if count == 2:
        print("Number is Prime")
    else:
        print("Not a Prime Number")

findPrime(nums);