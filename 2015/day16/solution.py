class AuntSue:
    def __init__(self, name: str, facts: dict):
        self.name = name
        self.facts = facts


class MFCSAM:
    def __init__(self):
        self.aunts = []
        self.criteria = {}
        self.best_guess = AuntSue

    def load_input(self, input: list[str]) -> None:
        for i in input:
            name = i.split(": ")[0]
            facts = {}
            for j in i.removeprefix(name + ": ").split(", "):
                key, value = j.split(": ")
                facts[key] = int(value)
            self.aunts.append(AuntSue(name, facts))

    def load_criteria(self, criteria: list) -> None:
        for c in criteria:
            key, value = c.split(": ")
            self.criteria[key] = int(value)

    def find_match(self) -> AuntSue:
        match = AuntSue
        for aunt in self.aunts:
            is_match = True
            for key, value in self.criteria.items():
                if key not in aunt.facts:
                    pass
                elif aunt.facts[key] != value:
                    is_match = False
            if is_match:
                match = aunt

        self.best_guess = match
        return match.name

    def find_match_part2(self) -> AuntSue:
        match = AuntSue
        greater, fewer = ["cats", "trees"], ["pomeranians", "goldfish"]
        for aunt in self.aunts:
            is_match = True
            for key, value in self.criteria.items():
                if key not in aunt.facts:
                    pass
                elif key in greater and not aunt.facts[key] > value:
                    is_match = False
                elif key in fewer and not aunt.facts[key] < value:
                    is_match = False
                elif aunt.facts[key] != value and key not in greater and key not in fewer:
                    is_match = False
            if is_match:
                match = aunt
        if match is not AuntSue:
            self.best_guess = match
            return match.name
        return None

if __name__ == '__main__':
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    puzzle_criteria = open("criteria.txt", "r").read().splitlines()
    mfcsam = MFCSAM()
    mfcsam.load_input(puzzle_input)
    mfcsam.load_criteria(puzzle_criteria)
    solution = mfcsam.find_match()

    print("solution: ", solution)

    solution2 = mfcsam.find_match_part2()
    print("Part2: ")
    print("solution: ", solution2)
