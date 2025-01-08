T = int(input())

for i in range(T):
  counter = 0
  answer = ''
  PS = input()
  for j in range(len(PS)):
    if PS[j] == '(':
      counter += 1
    else:
      counter -= 1
    
    if counter < 0:
      answer = 'NO'
      break

  if counter != 0:
    answer = 'NO'
  else:
    answer = 'YES'
  
  print(answer)