n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

tQuantity = 0

for size in sizes:  
  tQuantity += size // t
  if (size % t != 0):
    tQuantity += 1

print(tQuantity)
print(n // p, n % p)