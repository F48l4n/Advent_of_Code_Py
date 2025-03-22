# region Part 1
def check_disallowed_strs(text: str) -> bool:
    disallowed_strs = ["ab", "cd", "pq", "xy"]
    str_is_disallowed = False
    for disallowed_str in disallowed_strs:
        if disallowed_str in text:
            str_is_disallowed = True
    return str_is_disallowed


def check_for_unique_vowels(text: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    for vowel in vowels:
        if vowel in text:
            num_vowels += 1
    return num_vowels > 2


def check_for_vowels(text: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    for char in text:
        if char in vowels:
            num_vowels += 1
    return num_vowels > 2


def check_for_repeating_letters(text: str) -> bool:
    num_repeats, last_char = 0, ''
    for char in text:
        if char == last_char and last_char != '':
            num_repeats += 1
        last_char = char
    return num_repeats > 0


def check_if_nice(text: str) -> bool:
    nice = check_for_vowels(text) and check_for_repeating_letters(text) and not check_disallowed_strs(text)
    return nice


def check_all(pi: list) -> int:
    nice_words = 0
    for word in pi:
        nice_words += check_if_nice(word)
    return nice_words


# endregion Part 1

if __name__ == '__main__':
    assert (check_for_vowels("aei")
            and check_for_vowels("xazegov")
            and check_for_vowels("aeiouaeiouaeiou")), \
        "Error: Vowlchecker couldn't solve"
    assert (check_for_repeating_letters("xx")
            and check_for_repeating_letters("abcdde")), \
        "Error: repeating letters couldn't solve"
    assert check_if_nice("ugknbfddgicrmopn"), "Error: Example 1 couldn't be solved"
    assert check_if_nice("aaa"), "Error: Example 2 couldn't be solved"
    assert not check_if_nice("jchzalrnumimnmhp"), "Error: Example 3 couldn't be solved"
    assert not check_if_nice("haegwjzuvuyypxyu"), "Error: Example 4 couldn't be solved"
    assert not check_if_nice("dvszwmarrgswjxmb"), "Error: Example 5 couldn't be solved"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    print("solution: ", check_all(puzzle_input))

    print("Part2: ")
    print("solution: ", )
