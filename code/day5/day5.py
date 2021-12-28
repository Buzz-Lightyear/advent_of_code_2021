"""
    It's a 1000 x 1000 grid
    If horizontal or vertical line, increment each point by 1
    Return no. of points with value > 1
"""

def main():
    grid = {}
    with open("input.txt", "r") as f:
        lines = [[[int(z) for z in y.split(',')] for y in x.rstrip().split(' -> ')] for x in f.readlines()]
        for (a, b), (c, d) in lines:
            if a == c:
                low = min(b, d)
                high = max(b, d)
                for y in range(low, high+1):
                    if (a,y) in grid:
                        grid[(a,y)] += 1
                    else:
                        grid[(a,y)] = 1
            elif b == d:
                low = min(a, c)
                high = max(a, c)
                for x in range(low, high+1):
                    if (x,b) in grid:
                        grid[(x,b)] += 1
                    else:
                        grid[(x,b)] = 1
            elif abs(a-c) == abs(b-d):
                # diagonal
                if a < c and b < d:
                    x = a
                    y = b
                    while x <= c and y <= d:
                        if (x,y) in grid:
                            grid[(x,y)] += 1
                        else:
                            grid[(x,y)] = 1
                        x += 1
                        y += 1
                elif a > c and b < d:
                    x = a
                    y = b
                    while x >= c and y <= d:
                        if (x,y) in grid:
                            grid[(x,y)] += 1
                        else:
                            grid[(x,y)] = 1
                        x -= 1
                        y += 1
                elif a < c and b > d:
                    x = a
                    y = b
                    while x <= c and y >= d:
                        if (x,y) in grid:
                            grid[(x,y)] += 1
                        else:
                            grid[(x,y)] = 1
                        x += 1
                        y -= 1
                else:
                    x = a
                    y = b
                    while x >= c and y >= d:
                        if (x,y) in grid:
                            grid[(x,y)] += 1
                        else:
                            grid[(x,y)] = 1
                        x -= 1
                        y -= 1
        
        sum = 0
        for (i, j) in grid:
            if grid[(i,j)] > 1:
                sum += 1
        
        print(sum)


if __name__ == '__main__':
    main()