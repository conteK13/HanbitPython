n, m = map(int, input().split())

result = 0
for i in range(n):
    card_data = map(int, input().split())
    min_value = min(card_data)
    result=max(result, min_value)

print(result)

result = 0 
for i in range(n):
    card_data = map(int, input().split())
    min_value = 10001
    for a in card_data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)