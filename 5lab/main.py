from algorithm import *


def generate_items():
    items = []
    for i in range(100):
        value = random.randint(2, 30)
        weight = random.randint(1, 20)
        item = Item(value, weight)
        items.append(item)
    return items


def main():
    items = generate_items()
    solve_knapsack_bee(items)


if __name__ == "__main__":
    main()
