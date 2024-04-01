#시각

"""n = int(input())"""
n = 5
count= 0


for h in range (n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
            #if '3' in str(h) or '3' in str(m) or '3' in str(s):
                count +=1

print(count)