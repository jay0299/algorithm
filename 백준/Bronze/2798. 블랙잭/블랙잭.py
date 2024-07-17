n, m = map(int, input().split())
numbers = list(map(int, input().split()))

highest = 0

for i in range(n - 2):
  for j in range(i + 1, n - 1):
    for k in range(j + 1, n):
      if (numbers[i] + numbers[j] + numbers[k] <= m):
        # max = numbers[i] + numbers[j] + numbers[k]
        highest = max(highest, numbers[i] + numbers[j] + numbers[k])

print(highest)