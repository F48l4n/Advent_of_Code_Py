class Cell:
    def __init__(self, lit: bool = False) -> None:
        self.lit = lit

    def light(self):
        self.lit = True

    def dark(self):
        self.lit = False


class Grid:
    def __init__(self, part2:bool = False) -> None:
        self.grid: list[list[Cell]] = []
        self.part2 = part2

    def load(self, pi: list[list[str]]):
        self.grid = []
        for row in pi:
            new_row = []
            for col in row:
                if col == '#':
                    new_row.append(Cell(True))
                else:
                    new_row.append(Cell(False))
            self.grid.append(new_row)

    def run_tick(self):
        new_grid = self.grid.copy()
        neighbour_grid = [[0 for j in range(len(new_grid[0]))] for i in range(len(new_grid))]
        for row in range(len(new_grid)):
            for col in range(len(new_grid[row])):
                neighbour_grid[row][col] = self.get_neighbours(row, col)
        for row_index, row in enumerate(new_grid):
            for col_index, col in enumerate(row):
                neighbour_count = neighbour_grid[row_index][col_index]
                if neighbour_count == 3:
                    new_grid[row_index][col_index].light()
                elif neighbour_count <= 1 or neighbour_count > 3:
                    new_grid[row_index][col_index].dark()
        self.grid = new_grid

    def tick_n_times(self, n: int, debug:bool = False):
        for _ in range(n):
            self.run_tick()
            if debug:
                self.print_grid()

    def get_neighbours(self, row, col) -> int:
        neighbours: list[Cell] = []
        for _row in range(row - 1, row + 2):
            for _col in range(col - 1, col + 2):
                if self.part2 and ((_row , _col) == (0,0) or  (_row , _col) == (0,len(self.grid[0])-1) or (_row , _col) == (len(self.grid)-1,0) or (_row , _col) == (len(self.grid)-1,len(self.grid[0])-1)):
                    if _row == row and _col == col:
                        return 3
                    neighbours.append(Cell(True))
                elif _row == row and _col == col:
                    pass
                elif _row < 0 or _col < 0 or _row >= len(self.grid) or _col >= len(self.grid[0]):
                    pass
                else:
                    neighbour = self.grid[_row][_col]
                    neighbours.append(neighbour)
        number_lit = 0
        for neighbour in neighbours:
            if neighbour.lit:
                number_lit += 1

        return number_lit

    def return_number_lit(self):
        number_lit = 0
        for row in self.grid:
            for col in row:
                if col.lit:
                    number_lit += 1
        return number_lit

    def print_grid(self):
        for row in self.grid:
            for col in row:
                if col.lit:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print('')


if __name__ == '__main__':
    test_input = [[".", "#", ".", "#", ".", "#"],
                  [".", ".", ".", "#", "#", "."],
                  ["#", ".", ".", ".", ".", "#"],
                  [".", ".", "#", ".", ".", "."],
                  ["#", ".", "#", ".", ".", "#"],
                  ["#", "#", "#", "#", ".", "."]]

    grid = Grid()
    grid.load(test_input)
    grid.tick_n_times(4)
    assert grid.return_number_lit() == 4, "Error: Example failed"
    test_input_2 = [["#", "#", ".", "#", ".", "#"],
                  [".", ".", ".", "#", "#", "."],
                  ["#", ".", ".", ".", ".", "#"],
                  [".", ".", "#", ".", ".", "."],
                  ["#", ".", "#", ".", ".", "#"],
                  ["#", "#", "#", "#", ".", "#"]]
    grid = Grid(part2=True)
    grid.load(test_input_2)
    grid.tick_n_times(5, debug=True)
    assert grid.return_number_lit() == 17, "Error: Example 2 failed"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    converted_puzzle_input = [[j for j in i] for i in puzzle_input]
    grid = Grid()
    grid.load(converted_puzzle_input)
    grid.tick_n_times(100)
    print("solution: ", grid.return_number_lit())

    grid = Grid(part2=True)
    grid.load(converted_puzzle_input)
    grid.tick_n_times(100)
    print("Part2: ")
    print("solution: ", grid.return_number_lit())
