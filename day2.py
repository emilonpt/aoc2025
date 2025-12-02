from utils import get_input

def solve(day_input: list[str], part: int) -> int:

    day_input = day_input[0].split(",")

    hits = []

    for i,r in enumerate(day_input):
        day_input[i] = [int(x) for x in r.split("-")]
        for n in range(day_input[i][0],day_input[i][1]+1):
            max_len = int(len(str(n))/2)
            if part == 1:
                if len(str(n))%2 == 0:
                    left = str(n)[:max_len]
                    right = str(n)[max_len:]
                    if left == right:
                        hits.append(n)
            else:
                for p in range(1,max_len+1):
                    pattern = str(n)[:p]
                    reps = int(len(str(n))//p)
                    if pattern*reps == str(n):
                        hits.append(n)
                        break

    return sum(hits)

if __name__ == '__main__':
    print("Part 1:", solve(get_input(2),1))
    print("Part 2:", solve(get_input(2),2))