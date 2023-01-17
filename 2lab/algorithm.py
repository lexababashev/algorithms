import os
import func_timeout
import psutil
import math
from time import time
from pyamaze import COLOR


class LabirintSearcher:
    def __init__(self, m):
        self.m = m

        self.start = (self.m.rows, self.m.cols)
        self.finish = (1, 1)

        self.iterations = 0
        self.start_time = time()
        self.stops = 0
        self.StatesAmount = 0
        self.states = []

        self.CanBeSolve = False
        self.path = {}

        self.color = COLOR.blue
        self.name = ""


    def __del__(self):
        print(f"memory used = {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2}")

    def limitedLDFS(self, limit):
        return func_timeout.func_timeout(60 * 30, self.LDFS, args=[limit])

    def LDFS(self, limit):
        self.color = COLOR.red
        self.name = "LDFS"

        stack = [(self.start, [self.start])]
        while stack:
            if psutil.Process(os.getpid()).memory_info().rss > 1024 ** 3:
                raise MemoryError("1 GB used")

            self.iterations += 1
            current, self.path = stack.pop()
            if current not in self.states:
                self.states.append(current)

            if len(self.path) - 1 == limit:
                self.stops += 1
                continue

            if current == self.finish:
                self.StatesAmount = len(self.states)
                self.CanBeSolve = True
                break

            neighbours = []
            for direction in 'ESNW':
                if self.m.maze_map[current][direction] == True:
                    if direction == 'E':
                        neighbour = (current[0], current[1] + 1)
                    elif direction == 'W':
                        neighbour = (current[0], current[1] - 1)
                    elif direction == 'N':
                        neighbour = (current[0] - 1, current[1])
                    elif direction == 'S':
                        neighbour = (current[0] + 1, current[1])

                    if neighbour not in self.path:
                        neighbours.append((neighbour, self.path + [neighbour]))

            stack += neighbours

#==============================================================================================================

    # Euclidean distance
    @staticmethod
    def h(point_a: tuple, point_b: tuple):
        return math.sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)

    def limitedRBFS(self):
        return func_timeout.func_timeout(60 * 30, self.RBFS)

    def RBFS(self):
        self.color = COLOR.green
        self.name = "RBFS"

        bound = self.h(self.start, self.finish)
        stack = [(self.start, [self.start], bound)]
        while stack:
            if psutil.Process(os.getpid()).memory_info().rss > 1024 ** 3:
                raise MemoryError("1 GB used")

            self.iterations += 1
            current, self.path, curr_bound = stack.pop()
            if current not in self.states:
                self.states.append(current)

            if current == self.finish:
                self.StatesAmount = len(self.states)
                self.CanBeSolve = True
                break

            neighbours = []
            for direction in 'ESNW':
                if self.m.maze_map[current][direction] == True:
                    if direction == 'E':
                        neighbour = (current[0], current[1] + 1)
                    elif direction == 'W':
                        neighbour = (current[0], current[1] - 1)
                    elif direction == 'N':
                        neighbour = (current[0] - 1, current[1])
                    elif direction == 'S':
                        neighbour = (current[0] + 1, current[1])

                    if neighbour not in self.path:
                        f_val = max(self.h(neighbour, self.finish) + len(self.path), curr_bound)
                        neighbours.append((neighbour, self.path + [neighbour], f_val))

            neighbours.sort(key=lambda x: x[2])
            stack += neighbours
