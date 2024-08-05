import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0] * n
v = [-1] * n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
            v[i] = j

max = 0
max_index = 0
for i in range(n):
    if d[i] > max:
        max = d[i]
        max_index = i
        
print(max)

sub_seq = []
def recur(index):
    if index == -1:
        return
    recur(v[index])
    sub_seq.append(str(a[index]))
recur(max_index)
print(' '.join(sub_seq))

