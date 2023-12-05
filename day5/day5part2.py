from tqdm import tqdm

from bisect import bisect_right

def make_maps(data):
    maps_list = []
    for line in data:
        dest_start, src_start, length = map(int, line.strip().split())
        maps_list.append((src_start, src_start + length, dest_start))
    maps_list.sort()
    return maps_list

def convert_range(start, length, maps):
    out_ranges = []
    i = 0
    while length > 0 and i < len(maps):
        src_start, src_end, dest_start = maps[i]
        if start >= src_end:
            i += 1
        elif start < src_start:
            if length <= src_start - start:
                out_ranges.append((start, length))
                return out_ranges
            else:
                out_ranges.append((start, src_start - start))
                length -= src_start - start
                start = src_start
        else:
            if length <= src_end - start:
                out_ranges.append((start - src_start + dest_start, length))
                return out_ranges
            else:
                out_ranges.append((start - src_start + dest_start, src_end - start))
                length -= src_end - start
                start = src_end
    if length > 0:
        out_ranges.append((start, length))
    return out_ranges

def read_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    seeds_line, *stages_lines = lines
    seeds = [(int(x), int(y)) for x, y in zip(*[iter(seeds_line.split(': ')[1].split())]*2)]

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

    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temp, temp_to_humidity, humidity_to_location = data

    soils = make_maps(seed_to_soil)
    fertilizers = make_maps(soil_to_fertilizer)
    waters = make_maps(fertilizer_to_water)
    lights = make_maps(water_to_light)
    temps = make_maps(light_to_temp)
    humids = make_maps(temp_to_humidity)
    locations = make_maps(humidity_to_location)

    ranges = seeds
    for maps in [soils, fertilizers, waters, lights, temps, humids, locations]:
        new_ranges = []
        for start, length in ranges:
            new_ranges.extend(convert_range(start, length, maps))
        ranges = new_ranges

    return min(start for start, length in ranges)

print(lowest_location('input.txt'))