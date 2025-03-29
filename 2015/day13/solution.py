import math


def load_puzzle_input(_input: list) -> list:
    output: list = []
    for i in _input:
        tmp_i = i.replace('.', '').strip().split(' ')
        person, other_person = tmp_i[0], tmp_i[-1]
        points = int(tmp_i[3])
        if "lose" in i:
            points = -points
        output.append((person, other_person, points))
    return output


def generate_lookup_table(_input: list) -> dict:
    lookup: dict = {}
    for i in _input:
        person, other_person, points = i
        lookup[person + "_" + other_person] = points
    return lookup


def get_all_possible_combinations(_input: list, person: str, first_person: str, number_other_persons: int,
                                  lookup_table: dict) -> list:
    possible_next_persons = []
    for i in _input:
        if (not i[1] == person) or i[1] == first_person:
            possible_next_persons.append(i)

    output = []
    for i in possible_next_persons:
        _person, other_person, change = i
        if len(possible_next_persons) == number_other_persons:
            if _person == person and other_person == first_person:
                change += lookup_table[first_person + "_" + person]
                output.append(((person, first_person), change))
        elif _person == person and other_person != first_person:
            for p in get_all_possible_combinations(possible_next_persons, other_person, first_person,
                                                   number_other_persons, lookup_table):
                persons, total_change = p
                persons = list(persons)
                persons.insert(0, person)
                total_change += change + lookup_table[other_person + "_" + _person]
                output.append((persons, total_change))

    return output


def get_perfect_seating(_input: list) -> int:
    person, other_person, starting_change = _input[0]
    lookup = generate_lookup_table(_input)
    possible_combinations = []
    for p in get_all_possible_combinations(_input, person, person, int(math.sqrt(len(_input))), lookup):
        possible_combinations.append(p)
    max_change = None
    for combination in possible_combinations:
        persons, total_change = combination
        if max_change is None or total_change > max_change:
            max_change = total_change
    return max_change


if __name__ == '__main__':
    assert load_puzzle_input(["Mallory would lose 89 happiness units by sitting next to George."]) == [
        ('Mallory', 'George', -89)]
    test_input = open("test_input.txt", "r").read().splitlines()
    test_input = load_puzzle_input(test_input)
    assert get_perfect_seating(test_input) == 330, "Error: Example failed"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    solution1 = get_perfect_seating(load_puzzle_input(puzzle_input))
    print("solution: ", get_perfect_seating(load_puzzle_input(puzzle_input)))

    puzzle_input += open("self_input.txt", "r").read().splitlines()
    converted_input = load_puzzle_input(puzzle_input)
    print("Part2: ")
    print("solution: ", get_perfect_seating(converted_input))

