red = 12
green = 13
blue = 14

possible_games_sum = 0

minimum_cubes_power_sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        games = line.split(': ')[1]
        parts = games.split('; ')
        min_red, min_green, min_blue = red, green, blue
        for part in parts:
            cubes = part.split(', ')
            for cube in cubes:
                number, color = cube.strip().split()
                number = int(number)
                if color == 'red':
                    min_red = min(min_red, red - number)
                elif color == 'green':
                    min_green = min(min_green, green - number)
                elif color == 'blue':
                    min_blue = min(min_blue, blue - number)
        min_red = red - min_red
        min_green = green - min_green
        min_blue = blue - min_blue
        power = min_red * min_green * min_blue
        minimum_cubes_power_sum += power

print(minimum_cubes_power_sum)
