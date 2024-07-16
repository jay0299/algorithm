n = int(input())
current_room = 1
distance = 1

# 아직 목적지 n번방까지 도달하지 못했으면 6의 distance배수만큼 더한 값의 방으로 이동
while n > current_room:
    current_room += 6 * distance
    distance += 1

print(distance)