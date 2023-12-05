from tqdm import tqdm

from bisect import bisect_right

def make_maps(data):
    maps_list = []
    for line in data:
        dest_start, src_start, length = map(int, line.strip().split())
        maps_list.append((src_start, src_start + length, dest_start))
    maps_list.sort()
    return maps_list

def convert(value, maps):
    i = bisect_right(maps, (value,))
    if i:
        src_start, src_end, dest_start = maps[i - 1]
        if src_start <= value < src_end:
            return value - src_start + dest_start
    return value


def read_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    seeds_line, *stages_lines = lines
    seeds = seeds_line.split(': ')[1].split()

    stages = []
    stage = []
    for line in stages_lines:
        if line.endswith(' map:'):
            if stage:
                stages.append(stage)
                stage = []
        elif line:
            stage.append(line)
    stages.append(stage)

    return seeds, stages


def lowest_location(filename):
    seeds, data = read_from_file(filename)
    print(seeds)

    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location = data
    print(seed_to_soil)

    soils = make_maps(seed_to_soil)
    print(soils)
    fertilizers = make_maps(soil_to_fertilizer)
    print(fertilizers)
    waters = make_maps(fertilizer_to_water)
    print(waters)
    lights = make_maps(water_to_light)
    print(lights)
    temps = make_maps(light_to_temp)
    print(temps)
    humids = make_maps(temp_to_humidity)
    print(humids)
    locations = make_maps(humidity_to_location)
    print(locations)

    locations_out = []

    for seed in tqdm(seeds):
        print(f"Seed: {seed}")

        soil = convert(int(seed), soils)
        print(f"Soil: {soil}")

        fertilizer = convert(soil, fertilizers)
        print(f"Fertilizer: {fertilizer}")

        water = convert(fertilizer, waters)
        print(f"Water: {water}")

        light = convert(water, lights)
        print(f"Light: {light}")

        tempt = convert(light, temps)
        print(f"Temperature: {tempt}")

        humid = convert(tempt, humids)
        print(f"Humidity: {humid}")

        location = convert(humid, locations)
        print(f"Location: {location}")

        locations_out.append(location)

    return min(locations_out)


print(lowest_location('input.txt'))