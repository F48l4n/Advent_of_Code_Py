
def get_visited_houses(moves: str) -> int:
    visited_houses = [(0, 0),]
    x, y = 0, 0
    for move in moves:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        visited_houses.append((x, y))
    return len(set(visited_houses))


def get_visited_houses_with_robot(moves: str) -> int:
    def get_new_xy(ox: int, oy: int, last_move: chr) -> tuple:
        if last_move == '^':
            oy += 1
        elif last_move == 'v':
            oy -= 1
        elif last_move == '>':
            ox += 1
        elif last_move == '<':
            ox -= 1
        return ox, oy

    visited_houses = [(0, 0),]
    x, y = 0, 0
    rx, ry = 0, 0
    for i, move in enumerate(moves):
        if i % 2 == 0:
            rx, ry = get_new_xy(rx, ry, move)
            visited_houses.append((rx, ry))
        else:
            x, y = get_new_xy(x, y, move)
            visited_houses.append((x, y))
    return len(set(visited_houses))



if __name__ == '__main__':
    assert get_visited_houses(">") == 2, "Error: Example 1 couldn't be solved"
    assert get_visited_houses("^>v<") == 4, "Error: Example 2 couldn't be solved"
    assert get_visited_houses("^v^v^v^v^v") == 2, "Error: Example 3 couldn't be solved"

    assert get_visited_houses_with_robot("^v") == 3, "Error: Part2 Example 1 couldn't be solved"
    assert get_visited_houses_with_robot("^>v<") == 3, "Error: Part2 Example 2 couldn't be solved"
    assert get_visited_houses_with_robot("^v^v^v^v^v") == 11, "Error: Part2 Example 3 couldn't be solved"
    print("All tests passed!")

    problem_input = open('input.txt').readline()
    print("solution: ", get_visited_houses(problem_input))

    print("Part2:")
    print("solution: ", get_visited_houses_with_robot(problem_input))
