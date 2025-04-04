
def convert_to_dict(conversion_list: list[str]) -> dict:
    converted_dict: dict[str:set] = {}
    for conversion in conversion_list:
        starting_material, product = conversion.split(' => ')
        if starting_material not in converted_dict:
            converted_dict[starting_material] = {product}
        else:
            converted_dict[starting_material].add(product)
    return converted_dict


def convert_one_molek_num_pos_versions(conversion_dict: dict[str:set], input_molek: str) -> int:
    def convert_to_list() -> list[str]:
        result = ''
        for index, letter in enumerate(input_molek):
            if letter.isupper() and index != 0:
                result += ' '
            result += letter
        return result.split()

    combinations: set = set()
    converted_list = convert_to_list()
    for index, molek in enumerate(converted_list):
        if molek not in conversion_dict:
            continue
        for product in conversion_dict[molek]:
            inserted_molek = converted_list.copy()
            inserted_molek[index] = product
            combinations.add("".join(inserted_molek))

    return len(combinations)


if __name__ == '__main__':
    test_input, test_molek = ["H => HO", "H => OH", "O => HH"], "HOH"
    assert convert_one_molek_num_pos_versions(convert_to_dict(test_input), test_molek) == 4
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    starting_molek = puzzle_input.pop()
    puzzle_input.pop()
    converted_dict = convert_to_dict(puzzle_input)
    print("solution: ", convert_one_molek_num_pos_versions(converted_dict, starting_molek))

    print("Part2: ")
    print("solution: ", )
