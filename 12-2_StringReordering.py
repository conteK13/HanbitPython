s = input()
result = []
num = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        num += int(i)

result.sort()

if num != 0:
    result.append(str(num))     #str(num)을 하지 않으면 TypeError: sequence item 4: expected str instance, int found

print(''.join(result))

