filepath="..\\data\\input05.txt"
test05_1 = "..\\test\\test05_1.txt"
test05_2 = "..\\test\\test05_2.txt"

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def get_mapping(lines: list[str]) -> list[dict[int, int]]:
    '''
    Gets the mapping from the input and the seeds. returns a tuple of the seeds and the mapping.
    
    '''
    seed_to_soil = dict()
    soil_to_fert = dict()
    fert_to_water = dict()
    water_to_light = dict()
    light_to_temp = dict()
    temp_to_humid = dict()
    humid_to_loc = dict()
    mappings = [seed_to_soil, soil_to_fert, fert_to_water,
        water_to_light, light_to_temp, temp_to_humid, humid_to_loc]
    
    j = -1
    for i, line in enumerate(lines):
        if i == 0:
            line = line.split(":")[1]
            seeds = [int(part) for part in line.split()]
        elif line == "":
            j += 1
        elif "map" in line:
            continue
        else:
            nums = line.split()
            dest, source, length = [int(num) for num in nums]
            mappings[j][source] = [dest, length]
    return seeds, mappings

def find_location(seed: int, mapping:dict) -> int:
    '''
    Gets the location a seed will be planted for a given seed number.

    Usage example:
    >>> _, mapping = get_mapping(read_input(test05_1))
    >>> find_location(79, mapping)
    82
    >>> find_location(14, mapping)
    43
    >>> find_location(55, mapping)
    86
    >>> find_location(13, mapping)
    35
    '''
    current = seed
    for i, current_dict in enumerate(mapping):
        for org_val, dest_vals in current_dict.items():
            #print(current)
            difference = current - org_val 
            dest, max_length = dest_vals
            if difference < 0:
                continue
            elif difference < max_length:
                current = dest + difference
                break
            else:
                continue
    return current
                
def part1(filepath):
    '''
    Determines the lowest location number of the initial seed numbers

    Usage example:
    >>> part1(test05_1)
    Part 1:
    The lowest location number for the initial seeds is 35.
    '''
    lines = read_input(filepath)
    seeds, mapping = get_mapping(lines)
    locations = []
    for seed in seeds:
        locations.append(find_location(seed, mapping))
    print("Part 1:")
    print(f"The lowest location number for the initial seeds is {min(locations)}.")

def part2(filepath):
    '''
    Determines the lowest location number with the range of seeds rules.

    Usage example:
    >>> part2(test05_1)
    Part 2:
    The lowest location number for the initials seeds is 46.
    '''
    lines = read_input(filepath)
    seeds, mapping = get_mapping(lines)
    location = 1000000000
    for i, seed in enumerate(seeds):
        if i%2 != 0:
            continue
        else:
            start, length = seed, seeds[i+1]
            for seed_num in range(start, start+length):
                location = min( location, find_location(seed_num, mapping))
                
    print("Part 2:")
    print(f"The lowest location number for the initial seeds is {location}.")

part1(filepath)
part2(filepath)