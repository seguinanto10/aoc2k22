f = open("input.txt", "r")
lines = f.readlines()

def transform_line_into_lists(line):
    both_elfes = line.split(",")
    first_elf = [int(x) for x in both_elfes[0].split("-")]
    second_elf = [int(x) for x in both_elfes[1].split("-")]
    first_elf_range = [i for i in range(first_elf[0], first_elf[1] + 1)]
    second_elf_range = [i for i in range(second_elf[0], second_elf[1] + 1)]
    return first_elf_range, second_elf_range

def get_number_of_overlap_plannings(lines):
    c = 0
    for line in lines:
        first_elf, second_elf = transform_line_into_lists(line)
        if set(first_elf).issubset(second_elf) or set(second_elf).issubset(first_elf):
            c = c + 1  
    return c

number_of_overlap_plannings = get_number_of_overlap_plannings(lines)
print("number_of_overlap_plannings : " + str(number_of_overlap_plannings))

#part2
def get_number_of_real_overlap_plannings(lines):
    c = 0
    for line in lines:
        first_elf, second_elf = transform_line_into_lists(line)
        if any(item in first_elf for item in second_elf):
            c = c + 1
    return c

number_of_real_overlap_plannings = get_number_of_real_overlap_plannings(lines)
print("number_of_real_overlap_plannings : " + str(number_of_real_overlap_plannings))
