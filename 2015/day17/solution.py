from itertools import count


def get_all_possible_combinations(total_volume: int, cups: list[int]) -> list[list[int]]:
    possible_combinations = []
    if len(cups) == 0:
        return [[]]
    if total_volume <= 0:
        return [[]]
    for i, cup in enumerate(cups):
        new_cups = cups.copy()
        new_cups = new_cups[i + 1:]
        for p in get_all_possible_combinations(total_volume - cup, new_cups):
            p = list(p)
            p.insert(0, cup)
            possible_combinations.append(p)
    filtered_list = []
    for p in possible_combinations:
        calculated_volume = 0
        for cup in p:
            calculated_volume += cup
        if calculated_volume == total_volume:
            filtered_list.append(p)
    return filtered_list


def get_all_possible_smallest_combinations(total_volume: int, cups: list[int]) -> int:
    combinations = get_all_possible_combinations(total_volume, cups)
    lengths = [len(i) for i in combinations]
    min_cups = min(lengths)
    min_length_count = lengths.count(min_cups)
    return min_length_count


if __name__ == '__main__':
    test_cups = [20, 15, 10, 5, 5]
    assert len(get_all_possible_combinations(25, test_cups)) == 4, "Error: Example failed"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    puzzle_input = list(map(int, puzzle_input))
    print("solution: ", len(get_all_possible_combinations(150, puzzle_input)))

    print("Part2: ")
    print("solution: ", get_all_possible_smallest_combinations(150, puzzle_input))
