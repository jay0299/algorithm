T = int(input())

for i in range(T):
  k = int(input())  # 층
  n = int(input())  # 호
  people = [i for i in range(1, n+1)] # 0층에 사는 사람들의 수로 리스트 초기화
  
  for x in range(0, k):
    for y in range(1, n):
      people[y] += people[y - 1]  # 1호부터 이전 호수의 집에 사는 사람의 수를 더해 다음층에 사는 사람들의 수를 계산

  print(people[-1]) # k층 n호에 사는 사람의 수 출력
