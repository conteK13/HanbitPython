#두 배열의 원소 교체

"""n, k = map(int, input().split())
a = list(int(input().split()))
b = list(int(input().split()))"""

n, k = 5,3
a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

