import numpy as np
arr = []
n = int(input("Enter number of elements for array:"))
for i in range(n):
    print(f"Enter element:{i+1}")
    a = int(input())
    arr.append(a)

array = np.array(arr)
print("Ascending order of array:",np.sort(array))
print("Descending order of array:",np.sort(array)[::-1])