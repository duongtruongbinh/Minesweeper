from itertools import combinations
from Problem.minesweeper_problem import MinesweeperProblem


class BacktrackingSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)
        self.preprocess()
        self.sorted_known_cells = sorted(self.known_cells.items(), key=lambda x: len(
            self.get_unknown_neighbors(x[0][0], x[0][1])))
        self.solution = None

    def get_position(self, x, y):
        return x * self.cols + y + 1

    def is_combination_valid(self, combination):
        for i, j in self.known_cells.keys():
            neighbors = self.get_unknown_neighbors(i, j)
            num_bombs_around = self.known_cells[(i, j)]

            count = sum(1 for x, y in neighbors if self.get_position(
                x, y) in combination)

            if count != num_bombs_around:
                return False
        return True

    def check_subproblem(self, combination, i, j, value):
        neighbors = self.get_unknown_neighbors(i, j)
        count = sum([1 for x, y in combination if (x, y) in neighbors])
        return count == value

    def check_combination(self):
        self.solution = [self.get_position(i, j) for i in range(
            self.rows) for j in range(self.cols) if self.state[i][j] == -1]
        return self.is_combination_valid(self.solution)

    def solve(self, index=0):
        if index == len(self.known_cells):
            return self.check_combination()

        (i, j), value = self.sorted_known_cells[index]

        neighbors = self.get_unknown_neighbors(i, j)
        unknown_neighbors = [(x, y)
                             for x, y in neighbors if self.state[x][y] != -1]
        value -= len(neighbors) - len(unknown_neighbors)

        for combination in combinations(unknown_neighbors, value):
            if self.check_subproblem(combination, i, j, value):
                self.assign_combination(combination)
                if self.solve(index + 1):
                    return True
                self.unassign_combination(combination)

        return False

    def assign_combination(self, combination):
        for neighbor in combination:
            self.state[neighbor[0]][neighbor[1]] = -1

    def unassign_combination(self, combination):
        for neighbor in combination:
            self.state[neighbor[0]][neighbor[1]] = 0


def solve_minesweeper_backtracking(state):
    solver = BacktrackingSolver(state)
    solver.solve()
    return solver.solution
