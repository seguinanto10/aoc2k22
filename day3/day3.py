f = open("input.txt", "r")
lines = f.readlines()


def get_common_carac_between_two_lines(line1, line2):
    dupplicates = []
    for car in line1:
        if car in line2:
            dupplicates.append(car)    
    return list(dict.fromkeys(dupplicates))

def get_common_carac(lines):
    cars = []
    for line in lines:
        first_comp = line[0 : int(len(line)/2)]
        second_comp = line[int(len(line)/2) : len(line)]
        cars.extend(get_common_carac_between_two_lines(first_comp, second_comp))
    return cars

def get_priority(cars):
    priorities = []
    for car in cars:
        if(car.isupper()):
            priorities.append(ord(car) - 38)
        else:
            priorities.append(ord(car) - 96)
    return priorities
cars = get_common_carac(lines)

priority = sum(get_priority(cars))

print("sum of priorities : " + str(priority))

#Part2
def get_badges(lines):
    badges = []
    lines_per_three = []
    for line in lines:
        lines_per_three.append(line)
        if len(lines_per_three) == 3:
            common_cars = ''.join(get_common_carac_between_two_lines(lines_per_three[0], lines_per_three[1]))
            dupplicates = get_common_carac_between_two_lines(common_cars, lines_per_three[2])
            lines_per_three = []
            badges.append(dupplicates[0])
    return badges

badges = get_badges(lines)

priority = sum(get_priority(badges))

print("sum of priorities of badges : " + str(priority))
        

