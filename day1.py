from utils import get_input

def solve(day_input: list[str], part: int) -> int:

    pos = 50

    zero_counter = 0

    for line in day_input:

        temp_pos = pos + (1 if line[0]=="R" else -1) * int(line[1:])

        pos = temp_pos % 100

        zero_counter += (pos == 0 if part == 1 else abs(temp_pos // 100))

    return zero_counter


if __name__ == '__main__':
    print("Part 1:", solve(get_input(1),1))
    print("Part 2:", solve(get_input(1),2))