import os


def get_floor(x: str) -> int:
    ob = x.count("(")
    cb = x.count(")")

    return ob - cb


def get_first_char_to_basement(x: str) -> int:
    current_floor = 0
    for i, char in enumerate(x):
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1
        if current_floor < 0:
            return i + 1


if __name__ == "__main__":
    assert get_floor("(())") == 0 and get_floor("()()") == 0, "Error: Example 1 doesn't compute"
    assert get_floor("(((") == 3 and get_floor("(()(()(") == 3, "Error: Example 2 doesn't compute"
    assert get_floor("))(((((") == 3, "Error: Example 3 doesn't compute"
    assert get_floor("())") == -1 and get_floor("))(") == -1, "Error: Example 4 doesn't compute"
    assert get_floor(")))") == -3 and get_floor(")())())") == -3, "Error: Example 4 doesn't compute"

    assert get_first_char_to_basement(")") == 1, "Error: Part2: Example 1 doesn't compute"
    assert get_first_char_to_basement("()())") == 5, "Error: Part2: Example 2 doesn't compute"

    puzzle_input = open("day1/input.txt", "r").readline()
    print("Puzzle Input:", puzzle_input)
    print("solution part1:", get_floor(puzzle_input))
    print("solution part2:", get_first_char_to_basement(puzzle_input))
