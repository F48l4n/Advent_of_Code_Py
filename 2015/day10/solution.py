def next_look_and_say(previous: str) -> str:
    output, last_char = "", ''
    same_char = 1
    for char in previous:
        if last_char == '':
            pass
        elif char != last_char:
            output += str(same_char) + last_char
            same_char = 1
        else:
            same_char += 1
        last_char = char
    output += str(same_char) + last_char
    return output


def look_and_say(starting: str, repeats: int) -> str:
    output = starting
    for i in range(repeats):
        output = next_look_and_say(output)
    return output


if __name__ == '__main__':
    assert next_look_and_say("1") == "11", "Error: Example 1 failed"
    assert next_look_and_say("11") == "21", "Error: Example 2 failed"
    assert next_look_and_say("21") == "1211", "Error: Example 3 failed"
    assert next_look_and_say("1211") == "111221", "Error: Example 4 failed"
    assert next_look_and_say("111221") == "312211", "Error: Example 5 failed"
    print("All test passed")

    puzzle_input = open("input.txt", "r").readline()
    print("solution: ", len(look_and_say(puzzle_input, 40)))

    print("Part2: ")
    print("solution: ", len(look_and_say(puzzle_input, 50)))
