
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

times = [int(time) for time in lines[0].split(': ')[1].split()]
print(times)

distances = [int(distance) for distance in lines[1].split(': ')[1].split()]
print(distances)

answer = 1
for race in range(len(times)):
    ways_to_win = 0
    for hold_time in range(times[race]):
        velocity = hold_time
        distance = velocity * (times[race]-hold_time)
        if distance > distances[race]:
            ways_to_win += 1

    answer *= ways_to_win

print(answer)