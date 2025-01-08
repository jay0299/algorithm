N, K = map(int, input().split())

def factorial(n):
  value = 1
  for i in range(2, n + 1):
    value = value * i

  return value

print(int(factorial(N) / (factorial(N - K) * factorial(K))))