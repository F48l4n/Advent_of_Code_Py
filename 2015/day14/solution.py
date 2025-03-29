class Reindeer:
    def __init__(self, name: str, speed: int, sprint_duration: int, rest_duration: int) -> None:
        self.name = name
        self.speed = speed
        self.sprint_duration = sprint_duration
        self.rest_duration = rest_duration
        self.currently_sprinting = True
        self.current_duration = sprint_duration
        self.distance = 0
        self.points = 0

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

    def add_point(self) -> None:
        self.points += 1

    def get_points(self) -> int:
        return self.points


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

    def run_race(self, ticks) -> None:
        for i in range(ticks):
            for reindeer in self.reindeers:
                reindeer.step()

            current_leads, lead_distance = list(), 0
            for reindeer in self.reindeers:
                distance = reindeer.get_distance()
                if distance > lead_distance:
                    current_leads = [reindeer]
                    lead_distance = distance
                elif distance == lead_distance:
                    current_leads.append(reindeer)
            for lead in current_leads:
                lead.add_point()

    def get_max_distance(self) -> int:
        max_distance = 0
        for reindeer in self.reindeers:
            distance = reindeer.get_distance()
            if distance > max_distance:
                max_distance = distance
        return max_distance

    def get_max_points(self) -> int:
        max_points = 0
        for reindeer in self.reindeers:
            points = reindeer.get_points()
            if points > max_points:
                max_points = points
        return max_points


if __name__ == '__main__':
    test_input = [
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
    ]
    test_race = Race()
    test_race.load_reindeers(test_input)
    test_race.run_race(1000)
    assert test_race.get_max_distance() == 1120, "Error, Example couldn't compute"
    assert test_race.get_max_points() == 689, "Error, Example 2 couldn't compute"
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    race = Race()
    race.load_reindeers(puzzle_input)
    race.run_race(2503)
    print("solution: ", race.get_max_distance())

    print("Part2: ")
    print("solution: ", race.get_max_points())
