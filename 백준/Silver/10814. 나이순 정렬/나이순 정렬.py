N = int(input())
users = []
for i in range(0, N):
  users.append(list(input().split()))
  users[i][0] = int(users[i][0])

users.sort(key = lambda x : x[0])

for i in range(0, N):
  print(users[i][0], users[i][1])