import sys

N = int(sys.stdin.readline())
list = [0] * 10001

for _ in range(N):
  index = int(sys.stdin.readline())
  list[index] += 1

for i in range(len(list)):
  if list[i] != 0:
    for j in range(list[i]):
      print(i)