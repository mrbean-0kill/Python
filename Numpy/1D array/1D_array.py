import numpy as np
arr = []
a = int(input("Enter number of elements in the array:"))
for i in range(a):
    b = int(input())
    arr.append(b)
array = np.array(arr)
print("1-D array:",array)
print(type(array))