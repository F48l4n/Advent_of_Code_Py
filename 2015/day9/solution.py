def convert_strings(inputs: list) -> list:
    connections = []
    for input_str in inputs:
        ab, distance = input_str.split(' = ')
        a, b = ab.split(' to ')
        connections.append((a, b, int(distance)))
        connections.append((b, a, int(distance)))
    return connections


def get_all_possible_connections(connections: list, connection: tuple) -> list:
    pre_node, node, distance = connection
    possible_connections = []
    for _p in connections:
        a, b, distance = _p
        if a != pre_node and b != pre_node and b != node:
            possible_connections.append(_p)

    all_possible_paths = []
    for p2 in possible_connections:
        if p2[0] == node:
            qs = get_all_possible_connections(possible_connections, p2)
            for q in qs:
                qn = [connection] + q
                all_possible_paths.append(qn)

    if len(all_possible_paths) == 0:
        return list([[connection]])
    #   print(f"c: {connection} :\n ", all_possible_paths, "\n possible_connections: \n", possible_connections)
    return all_possible_paths


def get_path_distances(puzzle_input: list) -> list[int]:
    connections = convert_strings(puzzle_input)

    possible_paths = get_all_possible_paths(connections)
    distances = []
    for path in possible_paths:
        distance = 0
        for c in path:
            distance += int(c[2])
        distances.append(distance)

    return distances


def get_all_possible_paths(connections: list) -> list:
    possible_paths = []
    for connection in connections:
        for pc in get_all_possible_connections(connections, connection):
            possible_paths.append(pc)

    return possible_paths


if __name__ == '__main__':
    test_inputs = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    assert min(get_path_distances(test_inputs)) == 605, "Error: Example Failed"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    print("solution: ", min(get_path_distances(puzzle_input)))

    print("Part2: ")
    print("solution: ", max(get_path_distances(puzzle_input)))
