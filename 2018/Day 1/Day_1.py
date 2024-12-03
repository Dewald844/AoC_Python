inputFile = open("/Users/dewaldhaasbroek/Code/AoCPy/2018/Day 1/input.txt").readlines()

def add_or_subtract(current_frequency, s):
    return current_frequency + int(s[1:]) if s[0] == '+' else current_frequency - int(s[1:])

def calculate_part_one (input_list):
    current_frequency = 0
    for s in input_list:
        current_frequency = add_or_subtract(current_frequency, s)
    print("Part 1 => :", current_frequency)

def calculate_part_two (input_list):
    visited_dict = {0:1}
    current_frequency = 0
    found_twice = 0

    while found_twice == 0:
        for s in input_list:
            current_frequency = add_or_subtract(current_frequency, s)
            elem_value = visited_dict.get(current_frequency, "not_present")
            if elem_value == "not_present":
                visited_dict[current_frequency] = 1
            else:
                visited_dict[current_frequency] = elem_value + 1
                found_twice = current_frequency
                break

    print("Part 1 => :", found_twice)

calculate_part_one(inputFile)
calculate_part_two(inputFile)