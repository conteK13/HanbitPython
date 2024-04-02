"""
n= int(input())
n_data = set(int(input().split()))
m = int(input())
m_data = list(int(input().split()))
"""

n = 5
n_data = [8, 3, 7, 9, 2]
m = 3
m_data = [5, 7, 9]

for i in m_data:
    if i in n_data:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
