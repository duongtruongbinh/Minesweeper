from itertools import combinations
from Problem.minesweeper_problem import MinesweeperProblem
from Problem.cnf import *


class BruteForceSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)

    def complete_model(self, assignment):
        # Node stores the value of each cell that we think is true
        # Now we need to fill in the rest of the unknown_cells with false assumption
        model = set(assignment)
        model.update(-val for val in self.unknown_cells if val not in assignment)
        return sorted(model, key=abs)

    def isValid(self, assignment):
        # Calculate the heuristic by counting the number of violated clauses
        # We only calculate the heuristic for the model that we think is true
        model = self.complete_model(assignment)
        return all(CNFCLause(clause).satisfy(model) for clause in self.cnf)

    def solve(self):
        for num_bombs in range(1, len(self.unknown_cells) + 1):
            for combination in combinations(self.unknown_cells, num_bombs):
                # if self.is_combination_valid(combination):
                #     return combination
                assignment = list(combination)
                if self.isValid(assignment):
                    return combination
        return None
 # def get_position(self, x, y):
    #     return x * self.cols + y + 1

    # def is_combination_valid(self, combination):
    #     for i, j in self.known_cells.keys():
    #         neighbors = self.get_unknown_neighbors(i, j)
    #         num_bombs_around = self.known_cells[(i, j)]

    #         count = sum(1 for x, y in neighbors if self.get_position(x, y) in combination)

    #         if count != num_bombs_around:
    #             return False
    #     return True


def solve_minesweeper_bruteforce(state):
    solver = BruteForceSolver(state)
    return solver.solve()
