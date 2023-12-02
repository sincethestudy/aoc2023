# 12 red cubes, 13 green cubes, and 14 blue cubes

red = 12
green = 13
blue = 14

possible_games_sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        print(line)
        games = line.split(': ')[1]
        parts = games.split('; ')
        combined_cubes = []
        for part in parts:
            combined_cubes.extend(part.split(', '))

        print(combined_cubes)
        
        game_id = int(line.split(':')[0].split(' ')[1])
        print(game_id)

        is_possible = True
        for cube in combined_cubes:
            number, color = cube.strip().split()
            print(color, number)
            number = int(number)
            if (color == 'red' and number > red) or \
                (color == 'green' and number > green) or \
                (color == 'blue' and number > blue):
                is_possible = False
                break
            if not is_possible:
                break
        if is_possible:
            possible_games_sum += game_id

    print(possible_games_sum)