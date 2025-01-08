N = int(input())
value = N
for i in range(1, N):
  value = value * (N - i)

counter = 0
value = str(value)
for i in range(1, len(value)):
  if value[-i] != '0':
    break
  counter += 1

print(counter)