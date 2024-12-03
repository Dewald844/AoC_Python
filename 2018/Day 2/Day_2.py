inputFile = open("/Users/dewaldhaasbroek/Code/AoCPy/2018/Day 2/input.txt").readlines()

def calculate_part_one(input):
    two_count = 0
    three_count = 0
    for s in input:
        char_count = {}
        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
        two_found = False
        three_found = False
        for key in char_count:
            if char_count[key] == 2 and not two_found:
                two_count += 1
                two_found = True
            if char_count[key] == 3 and not three_found:
                three_count += 1
                three_found = True
    print("Part 1 => :", two_count * three_count)

def calculate_part_two(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            diff = 0
            min_length = min(len(input[i]), len(input[j]))
            for k in range(min_length):
                if input[i][k] != input[j][k]:
                    diff += 1
            if diff == 1:
                print("Part 2 => :", "".join([input[i][k] for k in range(min_length) if input[i][k] == input[j][k]]))

calculate_part_one(inputFile)
calculate_part_two(inputFile)