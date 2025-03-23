class Grid:
    def __init__(self):
        self.grid = [[Light() for j in range(1000)] for i in range(1000)]

    def toggle(self, sx, ex, sy, ey) -> None:
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                self.grid[i][j].toggle()

    def turn_on(self, sx, ex, sy, ey) -> None:
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                self.grid[i][j].turn_on()

    def turn_off(self, sx, ex, sy, ey) -> None:
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                self.grid[i][j].turn_off()

    def num_on(self) -> int:
        num_on = 0
        for x in self.grid:
            for y in x:
                num_on += y.is_on()
        return num_on

    def print_grid(self):
        for x in self.grid:
            line = ""
            for y in x:
                line += str(int(y.is_on()))
            print(line)


class Light:
    def __init__(self):
        self.lit = 0

    def toggle(self):
        self.lit += 2

    def turn_on(self):
        self.lit += 1

    def turn_off(self):
        self.lit = max(self.lit - 1, 0)

    def is_on(self):
        return self.lit


def instruction_to_action(instruction: str, grid: Grid):
    def to_coords(coord_string: str) -> [int, int, int, int]:
        coords = coord_string.split(' through ')
        _sx, _sy = map(int, coords[0].split(','))
        _ex, _ey = map(int, coords[1].split(','))
        return _sx, _ex, _sy, _ey

    if instruction.startswith('turn on'):
        sx, ex, sy, ey = to_coords(instruction[8:])
        grid.turn_on(sx, ex, sy, ey)
        return

    if instruction.startswith('turn off'):
        sx, ex, sy, ey = to_coords(instruction[9:])
        grid.turn_off(sx, ex, sy, ey)
        return

    if instruction.startswith('toggle'):
        sx, ex, sy, ey = to_coords(instruction[7:])
        grid.toggle(sx, ex, sy, ey)
        return

    Exception("instruction couldn't be parsed, instruction :", instruction)


def run_all_instructions_print_on(instructions: list) -> int:
    grid = Grid()
    for instruction in instructions:
        instruction_to_action(instruction, grid)

    return grid.num_on()


if __name__ == '__main__':
    assert run_all_instructions_print_on(["turn on 0,0 through 999,999"]) == 1000000, \
        "Error: Example 1 couldn't be solved"
    assert run_all_instructions_print_on(["toggle 0,0 through 999,0"]) == 2000, \
        "Error: Example 2 couldn't be solved"
    assert run_all_instructions_print_on(["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"]) == 1000000-4, \
        "Error: Example 3 couldn't be solved"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    print("solution: ", run_all_instructions_print_on(puzzle_input))

