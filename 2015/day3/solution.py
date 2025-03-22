
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


if __name__ == '__main__':
    assert get_visited_houses(">") == 2, "Error: Example 1 couldn't be solved"
    assert get_visited_houses("^>v<") == 4, "Error: Example 2 couldn't be solved"
    assert get_visited_houses("^v^v^v^v^v") == 2, "Error: Example 3 couldn't be solved"
    print("All tests passed!")

    problem_input = open('input.txt').readline()
    print("solution: ", get_visited_houses(problem_input))
