from utils import get_input


def get_neighbours(coords: tuple, grid: dict) -> list[str]:

    neighbours = []
    
    x_max = max([x for x in [k[0] for k in grid.keys()]])
    y_max = max([y for y in [k[1] for k in grid.keys()]])

    (x,y) = coords

    for p in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:

        p_x = p[0]
        p_y = p[1]

        if 0 <= p_x <= x_max and 0 <= p_y <= y_max:

            neighbours.append(grid[(p_x,p_y)])

    return neighbours


def mark_accessibles(grid: dict) -> dict:

    x_max = max([x for x in [k[0] for k in grid.keys()]])
    y_max = max([y for y in [k[1] for k in grid.keys()]])

    for point in grid.keys():

        (x,y) = point

        counter = 0

        for p in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:

            p_x = p[0]
            p_y = p[1]

            if 0 <= p_x <= x_max and 0 <= p_y <= y_max:

                if grid[(p_x,p_y)] == "@":
                    
                    counter += 1

        if counter < 4 and (grid[(x,y)] == "@" or grid[(x,y)] == "x"):
            if grid[(x,y)] == "x":
                grid[(x,y)] = "."
            
            if  grid[(x,y)] == "@":
                grid[(x,y)] = "x"

    return grid

def solve(day_input: list[str], part: int,) -> int:

    grid = dict()
    for y,row in enumerate(day_input):
        for x,_ in enumerate(row):
            grid[(x,y)] = row[x]

    res = 0

    init = list(grid.values()).count("@")

    for point in grid.keys():

        if grid[point] == "@":

            if part == 1:
                res = res + (1 if get_neighbours(point, grid).count("@") < 4 else 0)

    if part == 2:

        grid = mark_accessibles(grid)

        while list(grid.values()).count("x") > 0:
            grid = mark_accessibles(grid)

        res = init - list(grid.values()).count("@")

    return res
        
if __name__ == '__main__':
    print("Part 1:", solve(get_input(4),1))
    print("Part 2:", solve(get_input(4),2))