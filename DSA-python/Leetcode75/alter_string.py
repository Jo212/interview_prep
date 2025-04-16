str1 = "abc"
str2 = "12345"
len1 = len(str1)
len2 = len(str2)
maxLength = max(len1, len2)
res = []
ind = 0
for i in range(maxLength):
    if i < len1:
        res.insert(ind,str1[i])
        ind = ind +1
    if i < len2:
        res.insert(ind,str2[i])
        ind = ind + 1
print("".join(res))