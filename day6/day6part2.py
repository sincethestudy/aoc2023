
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

times = [int(time) for time in lines[0].split(': ')[1].split()]
print(times)

distances = [int(distance) for distance in lines[1].split(': ')[1].split()]
print(distances)


times_str = ''.join(map(str, times))
distances_str = ''.join(map(str, distances))


ways_to_win = 0
for hold_time in range(int(times_str)):
    velocity = hold_time
    distance = velocity * (int(times_str)-hold_time)
    if distance > int(distances_str):
        ways_to_win += 1


print(ways_to_win)