filepath="..\\data\\input07.txt"

def read_input(filepath):
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return lines

def get_directories(lines):

    cwd =""
    go_up = ".."
    home = "/home"
    empty = ""
    dir = "dir"
    directories = {home: 0}
    

    for line in lines:
        parts = line.split()

        if "ls" in parts:
            pass
        else:
            if parts[0] == "$":
                if parts[2] == go_up:
                    # find a / and go up to that directory
                    cwd = cwd[:cwd.rindex("/")]
                elif parts[2] == "/":
                    cwd = home
                else:
                    cwd = cwd + "/" + parts[2]
                    directories[cwd] = 0
            else:
                # now we start adding the sub directories count
                if parts[0] != dir:
                    temp = cwd
                    while temp != empty:
                        directories[temp] += int(parts[0])
                        temp = temp[:temp.rindex("/")]

    return directories


def part1(filepath):

    lines = read_input(filepath)
    directories = get_directories(lines)
    cutoff = 100000

    sum_small_dir = 0
    for _, size in directories.items():
        if size < cutoff:
            sum_small_dir += size
            
    print("Part 1:")
    print(f"The total size of the small directories is : {sum_small_dir}.")

def part2(filepath):

    home = "/home"
    lines = read_input(filepath)
    directories = get_directories(lines)
    target = directories[home] - (70000000 - 30000000)
    smallest_dir = directories[home]
    for _, size in directories.items():
        if target < size < smallest_dir:
            smallest_dir = size

    print("Part 2:")
    print(f"The total size of that directory is: {smallest_dir}")

part1(filepath)
part2(filepath)

