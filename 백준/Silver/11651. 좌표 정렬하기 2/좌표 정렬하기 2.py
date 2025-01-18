import sys

coordinates = []
N = int(sys.stdin.readline())
for i in range(N):
  coordinates.append(list(map(int, sys.stdin.readline().split())))

coordinates.sort(key = lambda x: (x[1], x[0]))

for coordinate in coordinates:
  print(coordinate[0], coordinate[1])
