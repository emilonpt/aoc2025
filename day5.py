from utils import get_input

def solve(day_input: list[str], part: int,) -> int:

    fresh = set()

    ranges = [(int(l.split("-")[0]), int(l.split("-")[1])) for l in day_input if "-" in l]

    ings_to_check = [int(i) for i in day_input if "-" not in i and i != '']

    for ing in ings_to_check:
        for r in ranges:
            if r[0] <= ing <= r[1]:
                fresh.update({int(ing)})

    if part == 2:
        total_count = 0
        for r in ranges:
            to_subtract = 0
            for rr in [rrr for rrr in ranges if rrr != r]:
                if rr[0] <= r[0] <= rr[1]:
                    overlap_start = r[0]
                    overlap_end = min(r[1],rr[1])
                    overlap_size = overlap_end-overlap_start+1

                    to_subtract += overlap_size
            total_count += r[1]-r[0]+1 - to_subtract

    #343802932613010 too high
    # for some reason above approach seems not to be working
    # so I was thinking just "collapsing"/uniting ranges where there's overlap in a new range list
    # and then in the end just count all items in the new range list

    return len(fresh) if part == 1 else total_count
        
if __name__ == '__main__':
    print("Part 1:", solve(get_input(5),1))
    print("Part 2:", solve(get_input(5),2))