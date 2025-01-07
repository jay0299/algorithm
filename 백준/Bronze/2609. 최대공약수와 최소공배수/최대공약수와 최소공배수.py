A, B = map(int, input().split())
gcf = 0 # 최대공약수 Greatest Common Factor
lcm = 10000 # 최소공배수 Lest Common Multiple

# 최대공약수 구하기
for i in range(1, min(A, B) + 1):
  if (A % i == 0 and B % i == 0): # i가 A와 B의 공약수일 때
    gcf = i

# 최소공배수 구하기
lcm = int(gcf * (A/gcf) * (B/gcf))

print(gcf)
print(lcm)