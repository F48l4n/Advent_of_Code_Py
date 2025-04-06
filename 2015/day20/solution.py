import numpy as np


def get_first_house_with_x_present(presents: int, presents_per_house: int = 10, part2: bool = False) -> int:
    max_house = presents // presents_per_house
    houses = [0 for _ in range(max_house + 1)]
    for number in range(1, max_house + 1):
        all_houses = np.arange(start=number, stop=max_house+1, step=number)
        if part2:
            all_houses = all_houses[:50]
        for house in all_houses:
            houses[house] += number * presents_per_house
    i = 0
    while houses[i] < presents:
        i += 1

    return i


if __name__ == '__main__':
    assert get_first_house_with_x_present(70) == 4, "Error: Example 1 couldn't be solved"
    assert get_first_house_with_x_present(120) == 6, "Error: Example 2 couldn't be solved"
    print("All test passed")

    puzzle_input = int(open("input.txt", "r").readline())
    print("solution: ", get_first_house_with_x_present(puzzle_input, 10))

    print("Part2: ")
    print("solution: ", get_first_house_with_x_present(puzzle_input, 11, True))
