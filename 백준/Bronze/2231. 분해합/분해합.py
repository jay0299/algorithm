n = int(input())

for i in range(1, n + 1):
  # 생성자를 찾기 위해 분해합을 i값으로 초기화
  sum = i
  # 변수 sum에 i를 이루는 각 자리수 합산
  for number in str(i):
    sum += int(number)
  
  # 분해합이 n과 같다면 i는 n의 생성자
  if (sum == n):
    print(i)
    break
  # 생성자가 없다면 0 출력
  elif (i == n and sum != n):
    print(0)