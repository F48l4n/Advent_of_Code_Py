import json


def get_sum(json_input: dict | list) -> int:
    total = 0
    if type(json_input) is list:
        for i in json_input:
            total += get_sum(i)
    elif type(json_input) is dict:
        for key in json_input:
            value = json_input[key]
            total += get_sum(value)
    elif type(json_input) is int:
        total += json_input
    return total


def get_sum_ignore_red(json_input: dict | list) -> int:
    total = 0
    if type(json_input) is list:
        for i in json_input:
            total += get_sum_ignore_red(i)
    elif type(json_input) is dict:
        mini_total, contains_red = 0, False
        for key in json_input:
            value = json_input[key]
            mini_total += get_sum_ignore_red(value)
            if value == "red":
                contains_red = True
        if not contains_red:
            total += mini_total
    elif type(json_input) is int:
        total += json_input
    return total


if __name__ == '__main__':
    print(get_sum([1, 2, 3]))
    assert get_sum([1, 2, 3]) == 6, "Error: Example 1 failed"
    assert get_sum({"a": 2, "b": 4}) == 6, "Error: Example 2 failed"
    assert get_sum([[[3]]]) == 3, "Error: Example 3 failed"
    assert get_sum({"a": {"b": 4}, "c": -1}) == 3, "Error: Example 4 failed"
    assert get_sum({"a": [-1, 1]}) == 0, "Error: Example 5 failed"
    assert get_sum([-1, {"a": 1}]) == 0, "Error: Example 6 failed"
    assert get_sum([]) == 0, "Error: Example 7 failed"
    assert get_sum({}) == 0, "Error: Example 8 failed"
    print("All test passed")

    puzzle_json = json.load(fp=open('input.json', "r"))
    print("solution: ", get_sum(puzzle_json))

    print("Part2: ")
    print("solution: ", get_sum_ignore_red(puzzle_json))
