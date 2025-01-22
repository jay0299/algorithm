import sys

N = int(sys.stdin.readline())
n = sorted([int(sys.stdin.readline()) for _ in range(N)])
dic = {}

for num in n:
  if num in dic:
    dic[num] += 1
  else:
    dic[num] = 1

freq_num = 0
same_freq_list = []
max_freq = max(dic.values())

for num in dic:
  if dic[num] == max_freq:
    same_freq_list.append(num)
    freq_num = num

if len(same_freq_list) > 1:
  freq_num = sorted(same_freq_list)[1]

print(round(sum(n)/N))  # 산술평균
print(n[N//2])  # 중앙값
print(freq_num) # 최빈값
print(max(n) - min(n))  # 범위