class Machine:
    def __init__(self):
        self.calculations = dict()
        self.results = dict()

    def parse_commands(self, commands: list) -> None:
        for command in commands:
            (operations, result) = command.split('->')
            self.calculations[result.strip()] = operations.strip().split(' ')

    def calculate(self, name: str) -> int:
        try:
            return int(name)
        except ValueError:
            pass

        if name not in self.results:
            operations = self.calculations[name]
            result = None
            if len(operations) == 1:
                result = self.calculate(operations[0])
            elif operations[0] == "NOT":
                result = ~self.calculate(operations[1]) & 0xffff
            elif operations[1] == "AND":
                result = self.calculate(operations[0]) & self.calculate(operations[2]) & 0xffff
            elif operations[1] == "OR":
                result = self.calculate(operations[0]) | self.calculate(operations[2]) & 0xffff
            elif operations[1] == "LSHIFT":
                result = self.calculate(operations[0]) << self.calculate(operations[2]) & 0xffff
            elif operations[1] == "RSHIFT":
                result = self.calculate(operations[0]) >> self.calculate(operations[2]) & 0xffff
            self.results[name] = result

        return self.results[name]


if __name__ == '__main__':

    puzzle_input = open("input.txt", "r").read().splitlines()
    machine = Machine()
    machine.parse_commands(puzzle_input)

    print("solution: ", machine.calculate('a'))

    print("Part2: ")
    machine2 = Machine()
    machine2.parse_commands(puzzle_input)
    machine2.results['b'] = machine.calculate('a')
    print("solution: ", machine2.calculate('a'))
