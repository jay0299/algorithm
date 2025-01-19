import sys
input = sys.stdin.readline

def custom_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

N = int(input())
diff = sorted([int(input()) for i in range(N)])

if len(diff) == 0:
  print(0)
else:
  cut = custom_round(N * 0.15)
  sum = 0
  num = 0
  for i in range(cut, N - cut):
    sum += diff[i]
    num += 1
  print(custom_round(sum / num))
