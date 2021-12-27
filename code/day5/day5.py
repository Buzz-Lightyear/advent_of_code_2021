"""
    It's a 1000 x 1000 grid
    If horizontal or vertical line, increment each point by 1
    Return no. of points with value > 1
"""

def main():
    with open("input.txt", "r") as f:
        lines = [[[int(z) for z in y.split(',')] for y in x.rstrip().split(' -> ')] for x in f.readlines()]
        print(lines[0])

if __name__ == '__main__':
    main()