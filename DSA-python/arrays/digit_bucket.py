def sumOfDigit (number):
    if number == 0:
        return 0
    return number % 10 + sumOfDigit(number//10)
arr = [1122,12345,23]
numb_dict = {}
for number in arr:
    numb_dict[number] = sumOfDigit(number)
sorted_dict = dict(sorted(numb_dict.items(), key=lambda  item: item[1]))
for k,v in sorted_dict.items():
    print(k)