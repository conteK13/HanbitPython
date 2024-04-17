#문자열 재정립
s = input()
data = []
num = 0

for i in s:
    if i.isalpha():
        data.append(i)
    else:
        num += int(i)

data.sort()

if num != 0:
    data.append(str(num))

print(''.join(data))
