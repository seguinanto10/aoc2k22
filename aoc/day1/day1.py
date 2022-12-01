f = open("input.txt","r")
lines = f.readlines()

def f(lines):
    Lines = []
    i = 0
    cpt = 0
    for line in lines:
        if line == '\n':
            Lines.append(cpt)
            i = i + 1
            cpt = 0
        else:
            cpt = cpt + int(line.replace('\n', ''))
    return Lines

Lines = f(lines)

max1 = max(Lines)
Lines.remove(max1)
max2 = max(Lines)
Lines.remove(max2)
max3 = max(Lines)

print("Max cal : " + str(max1))
print("Top 3 max cal : " + str(max1 + max2 + max3))