import sys
from collections import deque

N = int(sys.stdin.readline())
nums = deque(i for i in range(1, N + 1))

while len(nums) != 1:
  nums.popleft()
  nums.rotate(-1)

print(nums[0])