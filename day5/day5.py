f = open("input.txt", "r")
lines = f.readlines()

def rearrange_lines(lines):
    boxes = []
    movements = []
    before = True
    for line in lines:
        before = (line != '\n')
        line = line.replace('\n', '')
        if before and movements == []:
            boxes.append(line)
        else:
            movements.append(line)
    movements = movements[1::]

    return boxes, movements


def rearrange_boxes(boxes):
    arranged_boxes = {}
    index_of_piles = boxes[len(boxes) - 1]
    boxes = boxes[0:len(boxes) - 1]
    number_of_piles = int(index_of_piles[len(index_of_piles) - 1])
    temp_boxes = []
    for box in boxes:
        temp_box = box.split('[')
        i = 0
        while i < len(temp_box):
            temp_box[i] = temp_box[i].replace(']', '')
            if '    ' in temp_box[i]:
                nb_of_empty = temp_box[i].count('    ')
                for n in range(nb_of_empty + 1):
                    if n == 0:
                        temp_box[i] = temp_box[i][0]
                    else:
                        temp_box.insert(i+n, "empty")

            i = i + 1
        if temp_box[0] == '' or temp_box[0] == ' ':
            temp_box.remove(temp_box[0])
        temp_boxes.append(temp_box)
    boxes = temp_boxes
    maxLength = max(len(box) for box in boxes)
    for i in range(len(boxes)):
        while len(boxes[i]) < maxLength:
            boxes[i].append('empty')

    for i in range(number_of_piles):
        for box in boxes:
            if box[i] != 'empty':
                if i in arranged_boxes.keys():
                    arranged_boxes[i].append(box[i])
                else:
                    arranged_boxes[i] = [box[i]]
    for key in arranged_boxes:
        arranged_boxes[key].reverse()
    return arranged_boxes


def rearrange_movements(movements):
    arranged_movement = {'number': [], 'from_movement': [], 'to_movement': []}
    for movement in movements:
        number, places = movement.split('from')
        number = number.replace('move ', '')
        number = number.replace(' ', '')
        from_movement, to_movement = places.split(' to ')
        from_movement = from_movement.replace(' ', '')
        arranged_movement['number'].append(int(number))
        arranged_movement['from_movement'].append(int(from_movement) - 1)
        arranged_movement['to_movement'].append(int(to_movement) - 1)
    return arranged_movement

def make_movement(movement, boxes):
    for m in range(movement['number']):
        box = boxes[movement['from_movement']].pop()
        boxes[movement['to_movement']].append(box)
    return boxes

def make_all_movements(arranged_movements, arranged_boxes):
    for i in range(len(arranged_movements['number'])):
        arranged_boxes = make_movement({
            'number': arranged_movements['number'][i],
            'from_movement': arranged_movements['from_movement'][i],
            'to_movement': arranged_movements['to_movement'][i],
        }, arranged_boxes)
    return arranged_boxes


boxes, movements = rearrange_lines(lines)
arranged_boxes = rearrange_boxes(boxes)
arranged_movements = rearrange_movements(movements)
final_boxes = make_all_movements(arranged_movements, arranged_boxes)

#Part2
def make_all_movements_3001(arranged_movements, arranged_boxes):
    for i in range(len(arranged_movements['number'])):
        arranged_boxes = make_movement_3001({
            'number': arranged_movements['number'][i],
            'from_movement': arranged_movements['from_movement'][i],
            'to_movement': arranged_movements['to_movement'][i],
        }, arranged_boxes)
    return arranged_boxes

def make_movement_3001(movement, boxes):
    if movement['number'] == 1:
        print(movement)
        boxes = make_movement(movement, boxes)
    else:
        move = []
        for m in range(movement['number']):
            move.append(boxes[movement['from_movement']].pop())
        boxes[movement['to_movement']].extend(move[::-1])
    return boxes

boxes, movements = rearrange_lines(lines)
arranged_boxes = rearrange_boxes(boxes)
arranged_movements = rearrange_movements(movements)
final_boxes = make_all_movements_3001(arranged_movements, arranged_boxes)
print(final_boxes)