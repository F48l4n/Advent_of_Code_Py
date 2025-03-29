class Reindeer:
    def __init__(self, name: str, speed: int, sprint_duration: int, rest_duration: int) -> None:
        self.name = name
        self.speed = speed
        self.sprint_duration = sprint_duration
        self.rest_duration = rest_duration
        self.currently_sprinting = True
        self.current_duration = sprint_duration
        self.distance = 0

    def step(self) -> None:
        if self.currently_sprinting and self.current_duration >= 1:
            self.current_duration -= 1
            self.distance += self.speed
        elif not self.currently_sprinting and self.current_duration >= 1:
            self.current_duration -= 1
        else:
            self.currently_sprinting = not self.currently_sprinting
            if self.currently_sprinting:
                self.current_duration = self.sprint_duration
            else:
                self.current_duration = self.rest_duration
            self.step()

    def get_distance(self) -> int:
        return self.distance


class Race:
    def __init__(self):
        self.reindeers = []

    def load_reindeers(self, reindeers: list) -> None:
        for reindeer in reindeers:
            name, rest = reindeer.split(" can fly ")
            speed, rest = rest.split(" km/s for ")
            sprint_duration, rest = rest.split(" seconds, but then must rest for ")
            rest_duration = rest.split(" ")[0]

            speed = int(speed)
            sprint_duration = int(sprint_duration)
            rest_duration = int(rest_duration)

            self.reindeers.append(Reindeer(name, speed, sprint_duration, rest_duration))

    def run_race(self, ticks) -> int:
        for i in range(ticks):
            for reindeer in self.reindeers:
                reindeer.step()

        max_distance = 0
        for reindeer in self.reindeers:
            distance = reindeer.get_distance()
            if distance > max_distance:
                max_distance = distance
        return max_distance


if __name__ == '__main__':
    test_input = [
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
    ]
    test_race = Race()
    test_race.load_reindeers(test_input)
    assert test_race.run_race(1000) == 1120, "Error, Example couldn't compute"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    race = Race()
    race.load_reindeers(puzzle_input)
    print("solution: ", race.run_race(2503))

    print("Part2: ")
    print("solution: ", )
