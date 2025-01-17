import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
sg_cards = sorted(deque(map(int, input().split())))
M = int(input())
cards = deque(map(int, input().split()))

dic = {}
for card in sg_cards:
  if card in dic:
    dic[card] += 1
  else:
    dic[card] = 1

for card in cards:
  if card in dic:
    print(dic[card], end = ' ')
  else:
    print(0, end = ' ')