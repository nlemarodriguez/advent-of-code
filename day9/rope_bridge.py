def is_adjacent(position1, position2):
    if position1[0] == position2[0] and abs(position1[1] - position2[1]) <= 1:
        return True
    elif position1[1] == position2[1] and abs(position1[0] - position2[0]) <= 1:
        return True
    elif abs(position1[0] - position2[0]) == 1 and abs(position1[1] - position2[1]) == 1:
        return True
    return False


def move_head(head_position, direction):
    if direction == "U":
        head_position[0] += 1
    elif direction == "R":
        head_position[1] += 1
    elif direction == "D":
        head_position[0] -= 1
    elif direction == "L":
        head_position[1] -= 1


with open("day9/data_1.txt") as f:
    lines = f.readlines()
    positions_visited = []

    head_position = [0, 0]
    last_head_position = [0, 0]
    tail_position = [0, 0]

    for line in lines:
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])

        for _ in range(distance):
            last_head_position = head_position.copy()
            move_head(head_position, direction)
            if not is_adjacent(head_position, tail_position):
                tail_position = last_head_position
            if tail_position not in positions_visited:
                positions_visited.append(tail_position)
            # print(f"Head: {head_position}, Tail: {tail_position}, Positions visited: {positions_visited}")

    print(f"Part 1: {len(positions_visited)}")
