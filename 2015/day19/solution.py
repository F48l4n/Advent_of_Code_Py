import re


def convert_to_dict(conversion_list: list[str]) -> dict:
    converted_dict: dict[str:set] = {}
    for conversion in conversion_list:
        starting_material, product = conversion.split(' => ')
        if starting_material not in converted_dict:
            converted_dict[starting_material] = {product}
        else:
            converted_dict[starting_material].add(product)
    return converted_dict


def convert_to_list(im) -> list[str]:
    result = ''
    for index, letter in enumerate(im):
        if letter.isupper() and index != 0:
            result += ' '
        result += letter
    return result.split()


def run_all_possible_conversions(conversion_table: dict, input_molek: list) -> set[str]:
    combinations: set = set()
    for index, molek in enumerate(input_molek):
        if molek not in conversion_table:
            continue
        for product in conversion_table[molek]:
            inserted_molek = input_molek.copy()
            inserted_molek[index] = product
            combinations.add("".join(inserted_molek))
    return combinations


def convert_one_molek_num_pos_versions(conversion_dict: dict[str:set], input_molek: str) -> int:
    converted_list = convert_to_list(input_molek)
    return len(run_all_possible_conversions(conversion_dict, converted_list))


def steps_to_medicine(conversion_dict: dict[str:set], product) -> int:
    # reimplemented solution from https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4nsdd
    def rep(x) -> str:
        nonlocal iteration
        iteration += 1
        return reversed_dict[x.group()]

    reversed_dict = dict()
    for value, keys in conversion_dict.items():
        rvalue = value[::-1]
        for key in keys:
            rkey = key[::-1]
            reversed_dict[rkey] = rvalue
    molekule = product[::-1]
    print(reversed_dict)

    iteration = 0
    while molekule != "e":
        molekule = re.sub('|'.join(reversed_dict.keys()), rep, molekule)
        if output_file is not None:
            output_file.write(molekule + "\n")
    return iteration


if __name__ == '__main__':
    output_file = open("output.txt", "w")
    test_input, test_molek = ["H => HO", "H => OH", "O => HH", "e => O", "e => H"], "HOH"
    assert convert_one_molek_num_pos_versions(convert_to_dict(test_input), test_molek) == 4

#   assert steps_to_medicine(convert_to_dict(test_input), test_molek) == 3
#   assert steps_to_medicine(convert_to_dict(test_input), "HOHOHO") == 6
#   the tests  above end in an infinite loop, because at a certain point it wants to replace the first H with e
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    starting_molek = puzzle_input.pop()
    puzzle_input.pop()
    converted_dict = convert_to_dict(puzzle_input)
    print("solution: ", convert_one_molek_num_pos_versions(converted_dict, starting_molek))

    print("Part2: ")
    print("solution: ", steps_to_medicine(converted_dict, starting_molek))
