import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
  N, M = map(int, input().split())
  priority = deque(list(map(int, input().split())))
  counter = 0

  while priority:
    max_prior = max(priority)
    front = priority.popleft()
    M -= 1  # front 하나 뽑았으니 M값에 -1
    
    if front == max_prior:  # 뽑은 카드가 가장 높은 중요도를 가질 때
      counter += 1
      if M < 0: # 뽑은 카드가 타겟 카드일 때
        print(counter)
        break
    else: # 뽑은 카드가 가장 높은 중요도를 가지지 않을 때
      priority.append(front)  # deque의 가장 뒤에 다시 추가
      if M < 0: # 뽑은 카드가 타겟 카드일 때
        M = len(priority) - 1 # M도 가장 뒤의 인덱스를 가지도록 초기화