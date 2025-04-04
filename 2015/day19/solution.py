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


def steps_to_medicine(conversion_dict: dict[str:set], product, debug_print=False, s_molek="e") -> int:
    results, iterations = set(s_molek), 0
    while product not in results:
        iterations += 1
        new_results = set()
        for result in results:
            [new_results.add(i) for i in run_all_possible_conversions(conversion_dict, convert_to_list(result))]
        results = new_results
        if debug_print:
            output_file.write(str(iterations) + " : \n")
            output_file.writelines(str(results))
            output_file.write("\n")

    return iterations


if __name__ == '__main__':
    test_input, test_molek = ["H => HO", "H => OH", "O => HH", "e => O", "e => H"], "HOH"
    assert convert_one_molek_num_pos_versions(convert_to_dict(test_input), test_molek) == 4

    assert steps_to_medicine(convert_to_dict(test_input), test_molek) == 3
    assert steps_to_medicine(convert_to_dict(test_input), "HOHOHO") == 6
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    output_file = open("output.txt", "w")
    starting_molek = puzzle_input.pop()
    puzzle_input.pop()
    converted_dict = convert_to_dict(puzzle_input)
    print("solution: ", convert_one_molek_num_pos_versions(converted_dict, starting_molek))

    print("Part2: ")
    print("solution: ", steps_to_medicine(converted_dict, starting_molek, debug_print=True))
