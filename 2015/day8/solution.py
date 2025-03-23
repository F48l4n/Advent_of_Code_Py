def hex_to_ascii(hex_string: str) -> chr:
    return chr(int(hex_string, 16))


def calculate_discrepancy(unconverted_string: str) -> int:
    unconverted_string = unconverted_string[1:-1]
    last_char, converted_string, pass_chars = '', "", 0
    for i, char in enumerate(unconverted_string):
        if pass_chars > 0:
            pass_chars -= 1
        elif char == '\\' and last_char == '\\':
            converted_string = converted_string[:-1]
            converted_string += char
            last_char = ''
        elif char == '"' and last_char == '\\':
            converted_string = converted_string[:-1]
            converted_string += char
            last_char = ''
        elif char == 'x' and last_char == '\\':
            converted_string = converted_string[:-1]
            pass_chars = 2
            last_char = ''
            converted_string += hex_to_ascii(unconverted_string[i + 1: i + 3])
        else:
            converted_string += char
            last_char = char

    return (len(unconverted_string) - len(converted_string)) + 2


def calculate_all(unconverted_strings: list) -> int:
    number_discrepancy = 0
    for unconverted_string in unconverted_strings:
        number_discrepancy += calculate_discrepancy(unconverted_string)
    return number_discrepancy


if __name__ == '__main__':
    puzzle_input = open("input.txt", "r").read().splitlines()
    print("solution: ", calculate_all(puzzle_input))

    print("Part2: ")
    print("solution: ", )
