import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
people = deque([i for i in range(1, N + 1)])
removed = deque([])

while len(people) > 1:
  people.rotate(-(K - 1))
  removed.append(people.popleft())
removed.append(people.pop())

print('<', end = '')
for i in range(len(removed)):
  if (i == len(removed) - 1):
    print(removed[i], end = '')
  else:
    print(removed[i], end = ', ')
print('>', end = '')