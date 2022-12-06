f = open("input.txt", "r")
lines = f.readlines()


def check_all_chars_differents(list):
    return len(list) == len(set(list))

def init(line, n):
    list_of_n_chars = []
    for i in range(n):
        list_of_n_chars.append(line[i])
    return list_of_n_chars

def f(line, n):
    list_of_n_chars = init(line, n)
    if check_all_chars_differents(list_of_n_chars):
        return n
    cpt = n
    for char in line[n:len(line)]:
        if check_all_chars_differents(list_of_n_chars):
            return cpt
        list_of_n_chars.remove(list_of_n_chars[0])
        list_of_n_chars.append(char)
        cpt = cpt + 1
    return "Not found"


print("start packet : " + str(f(lines[0], 4)))
print("start message : " + str(f(lines[0], 14)))
