# Set 

# myset  = {"Hello",1, 2, 3,4, 4, 6,5, "hello", "Hello"}

# print(myset)


# nested loop 
myList = [1,2,3,4,5]

firstLoop = 0
secondLoop = 0
# 1 -
for i in myList: 
    firstLoop += 1
    for j in myList:
        secondLoop += 1
        for p in myList:
            print(i, j)

print("First Loop Count:", firstLoop)
print("Second Loop Count:", secondLoop)