import hashlib


def get_first_md5_with_leading_zeroes(salt: str, num_zeros: int = 5) -> int:
    pepper = 0
    solution_found = False
    leading_zeros = '0' * num_zeros

    while not solution_found:
        whole_string = salt + str(pepper)
        if hashlib.md5(whole_string.encode()).hexdigest()[:num_zeros] == leading_zeros:
            solution_found = True
            pass
        else:
            pepper += 1

    return pepper


if __name__ == "__main__":
    assert get_first_md5_with_leading_zeroes("abcdef") == 609043, "Error: Example 1 couldn't be solved"
    assert get_first_md5_with_leading_zeroes("pqrstuv") == 1048970, "Error: Example 2 couldn't be solved"
    print("All tests passed")

    puzzle_input = open("input.txt", "r").readline()
    print("solution: ", get_first_md5_with_leading_zeroes(puzzle_input))

    print("Part 2: ")
    print("solution: ", get_first_md5_with_leading_zeroes(puzzle_input, 6))
