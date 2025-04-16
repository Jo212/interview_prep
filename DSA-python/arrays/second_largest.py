import numpy as np

arr = np.array([7,0,0,0,0,0,7])
largest = 0
sec_largest = -1

for x in arr:
    if x > largest:
        sec_largest = largest
        largest = x
        print(sec_largest)
    if x > sec_largest and x < largest:
        sec_largest = x
print(sec_largest)
