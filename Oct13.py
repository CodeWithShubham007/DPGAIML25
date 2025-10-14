# Recursion in python - it is a python programming technique where a function calls itself to 
# solve problems by breaking them into smaller identical suebproblems units a simple based cased.

# factorial - 1
# def fac_cal(n):
#     fact = 1;
#     for i in range(1, n + 1):
#         fact *= i
#     return fact;

# data = fac_cal(5)
# print(data)

# print(fac_cal(5))

# factorial - 2

def fact_cal(n):
    if n == 1:
        return 1
    else:
        return n * fact_cal(n - 1)


# print(fact_cal(6))

# sorting
# 1. Bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr[j] = arr[j] + arr[j + 1]
                arr[j + 1] = arr[j] - arr[j + 1]
                arr[j] = arr[j] - arr[j + 1]
    return arr
# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]));

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)

insertion_sort([12, 11, 13, 5, 6])