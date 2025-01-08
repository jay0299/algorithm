N = int(input())
coordinates = []
for i in range(N):
  coordinates.append(list(map(int, input().split())))

coordinates.sort(key = lambda x: (x[0], x[1]))

for coordinate in coordinates:
  print(coordinate[0], coordinate[1])