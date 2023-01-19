from Bee import *

EXPLORERS = 100
FORAGERS = 100
MY_FUNC_GOAL = 870


def generate_explorer_bees(items):
    engaged_positions = []
    explorers = []

    min_value = len(items)
    if EXPLORERS + 1 < len(items):
        min_value = EXPLORERS + 1

    for i in range(min_value - 1):
        position = random.randint(0, len(items) - 1)
        while position in engaged_positions:
            position = random.randint(0, len(items) - 1)

        explorer = ExplorerBee(position, items[position])
        explorers.append(explorer)
        engaged_positions.append(position)
    return explorers


def generate_forager_bees():
    foragers = []
    for i in range(FORAGERS):
        forager = ForagerBee(0)
        foragers.append(forager)
    return foragers


def collect_items_info(explorers):
    information = []
    for explorer in explorers:
        information.append(explorer.collect_info())
    return information


def find_best_item(explorers):
    foragers = generate_forager_bees()
    information = collect_items_info(explorers)
    foragers_goes(foragers, explorers, information)
    foragers_accumulation = most_visited_item(foragers)
    return foragers_accumulation


def most_visited_item(foragers):
    accumulation = {}
    for forager in foragers:
        if forager.position not in accumulation:
            accumulation[forager.position] = 1
        else:
            accumulation[forager.position] += 1
    return max(accumulation)


def foragers_goes(foragers, explorers, information):
    for forager in foragers:
        forager.find_the_way(information, explorers)


def solve_knapsack_bee(generated_items):
    current_goal_function_value = 0
    iterations = 0
    while current_goal_function_value < MY_FUNC_GOAL:
        items = generated_items.copy()
        backpack = Backpack()

        while True:
            explorers = generate_explorer_bees(items)
            foragers_accumulation = find_best_item(explorers)
            if backpack.weight + items[foragers_accumulation].weight > backpack.max_weight:
                break
            backpack.put_in(items[foragers_accumulation])
            items.pop(foragers_accumulation)

        current_goal_function_value = backpack.value
        iterations += 1

    print(f"items:")
    count = 0
    for item in backpack.items:
        count += 1
        print(f"{count}) value = {item.value} weight = {item.weight}")
    print(f"\nfinal backpack value = {backpack.value}\n"
          f"final backpack weight = {backpack.weight}\n"
          f"avg value = {round(backpack.value / len(backpack.items), 2)}\n"
          f"avg weight = {round(backpack.weight / len(backpack.items), 2)}\n"
          f"amount of iterations = {iterations}\n")