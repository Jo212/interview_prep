s = "iceCreAM"
vowels = "AEIOUaeiou"
vowel_list = []
result = []
for ch in s:
    if ch in vowels:
        vowel_list.append(ch)
print(vowel_list)
for ch in s:
    if ch in vowels:
        result.append(vowel_list.pop())
    else:
        result.append(ch)
print("".join(result))