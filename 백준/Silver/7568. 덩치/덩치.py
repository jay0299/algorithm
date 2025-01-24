import sys

N = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for target in info:
  counter = 1
  for comp in info:
    if target[0] < comp[0] and target[1] < comp[1]:
      counter += 1
  print(counter, end = ' ')