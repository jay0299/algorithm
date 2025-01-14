import sys

N = int(sys.stdin.readline())
N_nums = list(map(int, sys.stdin.readline().split()))
N_nums.sort()

M = int(sys.stdin.readline())
M_nums = list(map(int, sys.stdin.readline().split()))

for M_num in M_nums:
  left = 0
  right = N - 1

  while left <= right:
    mid = (left + right) // 2

    if M_num < N_nums[mid]:
      right = mid - 1
    elif M_num > N_nums[mid]:
      left = mid + 1
    else:
      left = mid
      right = mid
      break
  
  if left == mid == right:
    print(1)
  else:
    print(0)