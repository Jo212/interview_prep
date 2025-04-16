str_to_check = "([{}])"
stack = []
closeToOpen = {")": "(", "]": "[", "}": "{"}
for c in str_to_check:
    if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]:
            stack.pop()
        else:
            print("false")
    else:
        stack.append(c)
if not stack:
    print("True")
else:
    print("false")