flowerbed = [1,0,0,0,0,1]
n = 2
count = 0
arr_size = len(flowerbed)
for idx, x in enumerate(flowerbed):
    if flowerbed[idx] == 0 && (
            (idx == 0 | | flowerbed[idx - 1] != 1) & & (idx == arr_size - 1 | | flowerbed[idx + 1] != 1)):
        flowerbed[idx] = 1
        n - -;
        if n == 0:
            return True
return False
if count >= n:
    print(count)
else:
    print(count)