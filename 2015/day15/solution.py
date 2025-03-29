import numpy as np


class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavour: int, texture: int, calories: int):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavour = flavour
        self.texture = texture
        self.calories = calories

    def get_all(self) -> list[int]:
        return [self.capacity, self.durability, self.flavour, self.texture, self.calories]


class Recipe:
    def __init__(self):
        self.ingredients = []
        self.best_mix = list
        self.best_score = int
        self.healthy_mix = list
        self.healthy_score = int

    def load_ingredient(self, ingredients: list[str]) -> None:
        for ingredient in ingredients:
            name, rest = ingredient.split(':')
            capacity, durability, flavour, texture, calories = rest.split(',')
            capacity = int(capacity.strip().split(' ')[1])
            durability = int(durability.strip().split(' ')[1])
            flavour = int(flavour.strip().split(' ')[1])
            texture = int(texture.strip().split(' ')[1])
            calories = int(calories.strip().split(' ')[1])
            self.ingredients.append(Ingredient(name, capacity, durability, flavour, texture, calories))

    def calculate_best_mix(self) -> None:
        # example data: [(14, Ingredient1), (86, Ingredient2)]
        def calculate_score(ratio_and_ingredients: list[tuple[int, Ingredient]]) -> tuple[int, int]:
            scores = []
            for i in ratio_and_ingredients:
                ratio, ingredient = i[0], i[1]
                total_score = [ratio * j for j in ingredient.get_all()]
                scores.append(total_score)

            total_score = scores.pop(0)
            for score in scores:
                total_score = np.add(score, total_score)
            for i, score in enumerate(total_score):
                if score < 0:
                    total_score[i] = 0

            return total_score[0] * total_score[1] * total_score[2] * total_score[3], total_score[4]

        def recursive_rest(iteration: int, rest: int) -> list[list[int]]:
            if iteration == len(self.ingredients):
                return [[rest]]
            combinations = []
            for i in np.arange(rest + 1):
                for j in recursive_rest(iteration + 1, rest - int(i)):
                    new_combination = j
                    new_combination.insert(0, int(i))
                    combinations.append(new_combination)
            return combinations

        all_combinations = recursive_rest(1, 100)
        best_mix = []
        best_score = 0

        healthy_mix = []
        healthy_score = 0
        for combination in all_combinations:
            final_combination = []
            for index, value in enumerate(combination):
                final_combination.append((value, self.ingredients[index]))
            score, calories = calculate_score(final_combination)
            if score > best_score:
                best_mix = final_combination
                best_score = score
            if calories == 500:
                if score > healthy_score:
                    healthy_mix = final_combination
                    healthy_score = score

        self.best_mix = best_mix
        self.best_score = best_score

        self.healthy_mix = healthy_mix
        self.healthy_score = healthy_score


if __name__ == '__main__':
    test_recipe = Recipe()
    test_recipe.load_ingredient(["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
                                 "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"])
    test_recipe.calculate_best_mix()
    assert test_recipe.best_score == 62842880, "Error: Example couldn't be calculated."
    assert test_recipe.healthy_score == 57600000, "Error: Example 2 couldn't be calculated."
    print("All test passed")

    puzzle_input = open("input.txt", "r").read().splitlines()
    recipe = Recipe()
    recipe.load_ingredient(puzzle_input)
    recipe.calculate_best_mix()

    print("solution: ", recipe.best_score)

    print("Part2: ")
    print("solution: ", recipe.healthy_score)
