N = int(input())
arr = []  # 배열 초기화

for i in range(0, N):
  arr.append(int(input()))
arr = sorted(arr) # 배열 정렬

# 결과 출력
for i in range (0, N):
  print(arr[i])