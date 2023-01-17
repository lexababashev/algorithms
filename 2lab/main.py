from pyamaze import maze, agent
from algorithm import LabirintSearcher
from time import time


def main():
    m = maze(30,50)
    m.CreateMaze()

    choose = 0
    while choose != 1 and choose != 2:
        choose = int(input("LDFS = 1\nRBFS = 2\nchoose algorithm = "))

    searcher = LabirintSearcher(m)
    if choose == 1:
        limit = 100
        searcher.limitedLDFS(limit)
        print(f"stops = {searcher.stops}")
        if not searcher.CanBeSolve:
            print("there is no solution with this limit")
    else:
        searcher.limitedRBFS()
        if not searcher.CanBeSolve:
            print("the agent did not reach the end")

    print(f"iterations = {searcher.iterations}")
    print(f"amount of states = {searcher.StatesAmount}")
    print(f"length result path = {len(searcher.path)}")
    print(f"{searcher.name} finised time = {time() - searcher.start_time} seconds")

    a = agent(m, shape='square', footprints=True, color=searcher.color)
    m.tracePath({a: searcher.path}, delay=100)
    m.run()


if __name__ == "__main__":
    main()

