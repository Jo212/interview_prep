arr = [1, 4, 6, 2, 3];
n = len(arr)
prefProduct = [1] * n
suffProduct = [1] * n
res = [0] * n
for i in range(n-2, -1,-1):
    suffProduct[i] = arr[i+1] * suffProduct[i+1]
for i in range(1,n):
    prefProduct[i] = arr[i-1] * prefProduct[i-1]
    print(prefProduct[i])