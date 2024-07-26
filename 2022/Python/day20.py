filepath="..\\data\\input20.txt"
test20 = "..\\test\\test20.txt"

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left
    
    def get_val(self):
        return self.val
    
    def set_left(self, other):
        self.left = other

    def set_right(self, other):
        self.right = other

    def set_val(self, val):
        self.val = val

def read_input(filepath) -> list[str]:
    
    with open(filepath, "r") as f:
        lines = f.readlines()

    return [i.strip() for i in lines]

def convert_to_linked_list(lines: list[str]) -> list[Node]:
    '''
    Converts the input to a list with all nodes and connects the nodes together as a linked list.
    '''
    linked_list = []
    for line in lines:
        new_node = Node(int(line))
        linked_list.append(new_node)
    
    for i, node in enumerate(linked_list):
        if i == 0:
            node.set_left(linked_list[-1])
            node.set_right(linked_list[1])
        elif i == len(linked_list) -1:
            node.set_left(linked_list[-2])
            node.set_right(linked_list[0])
        else:
            node.set_left(linked_list[i-1])
            node.set_right(linked_list[i+1])

    return linked_list

def shift_entries(linked_list: list[Node]):
    '''
    Rotates the entries of the linked list by the val of the node.
    ''' 
    N = len(linked_list)-1
    for i in range(len(linked_list)):
        
        node = linked_list[i]
        val = node.get_val()
        if val == 0 :
            continue
        
        if val < 0:
            val = abs(val)
            for _ in range(val%N):
                # get the three nodes of interest
                current_right = node.get_right()
                current_left = node.get_left()
                next_left = current_left.get_left()
                # connect the three nodes correctly
                current_right.set_left(current_left)
                current_left.set_right(current_right)
                current_left.set_left(node)
                node.set_right(current_left)
                node.set_left(next_left)
                next_left.set_right(node)
                
                
        else :
            for _ in range(val%N):
                # get the three nodes of interest
                current_right = node.get_right()
                current_left = node.get_left()
                next_right = current_right.get_right()
                # connect the three nodes correctly
                current_right.set_left(current_left)
                current_left.set_right(current_right)
                current_right.set_right(node)
                node.set_left(current_right)
                node.set_right(next_right)
                next_right.set_left(node)

    return linked_list
            
def part1(filepath):
    '''
    Gets the sum of the coordinates by looking at the numbers at the 1000th, 2000th and 3000th numbers after 0.

    Usage example:
    >>> part1(test20)
    Part 1:
    The sum of the three numbers that form the grove coordinates is 3
    '''

    lines = read_input(filepath)
    linked_list = convert_to_linked_list(lines)
    rotated = shift_entries(linked_list)
    total = 0
    for node in rotated:
        val = node.get_val()
        if val == 0:
            for i in range(3001):
                if i in [1000, 2000, 3000]:
                    total += node.get_val()
                node = node.get_right()
    print("Part 1:")
    print(f"The sum of the three numbers that form the grove coordinates is {total}")

def part2(filepath):
    '''
    Finds the sum of the three grove coordinates after multiplying with the key and mixing the list 10 times.

    Usage example:
    >>> part2(test20)
    Part 2:
    The sum of the three numbers that form the grove coordinates is 1623178306
    '''
    lines = read_input(filepath)
    linked_list = convert_to_linked_list(lines)
    key = 811589153
    vals = [node.get_val() for node in linked_list]
    final_vals = [val*key for val in vals]
    for i, node in enumerate(linked_list):
        current_val = node.get_val()
        new_val = current_val*key
        node.set_val(new_val)

    rotated = shift_entries(linked_list)
    for _ in range(9):
        rotated = shift_entries(rotated)
    for i, node in enumerate(rotated):
        node.set_val(final_vals[i])
    total = 0
    for node in rotated:
        val = node.get_val()
        if val == 0:
            for i in range(3001):
                if i in [1000, 2000, 3000]:
                    total += node.get_val()
                node = node.get_right()
    print("Part 2:")
    print(f"The sum of the three numbers that form the grove coordinates is {total}")




part1(filepath)
part2(filepath)
            
            
    


