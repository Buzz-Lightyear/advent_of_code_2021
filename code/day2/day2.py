def get_position_product():
    pos = [0,0]
    with open("input.txt") as f:
        lines = [x.rstrip().split(' ') for x in f.readlines()]
        for command, distance in lines:
            if command == 'forward':
                pos[0] += int(distance)
            elif command == 'up':
                pos[1] -= int(distance)
            else:
                pos[1] += int(distance)
    return pos[0] * pos[1]

def get_position_with_aim():
    hor = 0
    ver = 0
    aim = 0
    with open("input.txt") as f:
        lines = [x.rstrip().split(' ') for x in f.readlines()]
        for command, distance in lines:
            if command == 'forward':
                hor += int(distance)
                ver += (aim * int(distance))
            elif command == 'up':
                aim -= int(distance)
            else:
                aim += int(distance)
    
    return hor * ver

if __name__ == '__main__':
    print(get_position_with_aim())
