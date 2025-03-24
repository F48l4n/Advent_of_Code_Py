def verify_password(password: str) -> bool:
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    last_char, pairs, previously_consecutive, contains_consecutive, previously_pair = '', 0, False, False, False
    for letter in password:
        if last_char == chr(ord(letter) - 1):
            if previously_consecutive:
                contains_consecutive = True
            else:
                previously_consecutive = True
        else:
            previously_consecutive = False
        if last_char == letter and not previously_pair:
            previously_pair = True
            pairs += 1
        else:
            previously_pair = False
        last_char = letter
    return contains_consecutive and pairs > 1


def get_next_password(password: str) -> str:
    def advance_char(char: chr, index: int) -> None:
        if char == 'z' and index >= 0:
            new_password[index] = 'a'
            advance_char(new_password[index - 1], index - 1)
        elif char != '' and index >= 0:
            new_password[index] = chr(ord(char) + 1)
        else:
            pass

    new_password = [i for i in password]
    advance_char(new_password[-1], len(new_password) - 1)
    while not verify_password(''.join(new_password)):
        advance_char(new_password[-1], len(new_password) - 1)
    return ''.join(new_password)


if __name__ == '__main__':
    assert verify_password("abcdffaa"), "Error: Example 1 failed"
    assert verify_password("ghjaabcc"), "Error: Example 2 failed"
    assert not verify_password("ghjacbcc"), "Error: Example 3 failed"

    assert get_next_password("abcdefgh") == "abcdffaa", "Error: Example 4 failed"
    assert get_next_password("ghijklmn") == "ghjaabcc", "Error: Example 5 failed"
    print("All test passed")

    puzzle_input = open("input.txt", "r").readline()
    next_password = get_next_password(puzzle_input)
    print("solution: ", next_password)

    print("Part2: ")
    print("solution: ", get_next_password(next_password))
