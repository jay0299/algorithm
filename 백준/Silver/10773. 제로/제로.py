import sys

list = []
K = int(sys.stdin.readline())

for i in range(K):
  k = int(sys.stdin.readline())
  if k == 0:
    list.pop()
  else:
    list.append(k)

sum = 0
for e in list:
  sum += e

print(sum)