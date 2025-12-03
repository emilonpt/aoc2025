from utils import get_input


def find_max_in_bank(bank: list[int]) -> int:

    try:
        return bank.index(max(bank))
    except ValueError:
        return None

def build_max(bank: list[int], curr: str, ignore: int = None) -> str:

    if "x" in curr:
        for c in curr:
            if c == "x":
                max_index = find_max_in_bank(bank) if ignore is None else find_max_in_bank([b for b in bank if b < ignore])
                if max_index <= len(bank) -curr.count("x"):
                    return build_max(bank[max_index+1:], curr.replace(c,str(bank[max_index]),1))
                else:
                    if ignore is None:
                        ignore = bank[max_index]
                    else:
                        ignore = [b for b in bank if b < ignore][max_index]
                    return build_max(bank, curr, ignore)
    else:
        return curr
        
def solve(day_input: list[str], part: int) -> int:

    max_list = []

    for bank in day_input:
        bank = [int(c) for c in bank]

        if part == 1:
            first_max_in_bank_index = find_max_in_bank(bank)

            if first_max_in_bank_index == len(bank) - 1:
                max_list.append(int(str(bank[find_max_in_bank(bank[:-1])])+str(bank[first_max_in_bank_index])))
            else:
                max_list.append(int(str(bank[first_max_in_bank_index])+str(bank[first_max_in_bank_index+find_max_in_bank(bank[first_max_in_bank_index+1:])+1])))

        if part == 2:
            max_list.append(int(build_max(bank,"xxxxxxxxxxxx")))

    return sum(max_list)

if __name__ == '__main__':
    print("Part 1:", solve(get_input(3),1))
    print("Part 2:", solve(get_input(3),2))
    #3121910778619 is too low