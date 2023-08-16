from itertools import combinations
from Problem.minesweeper_problem import MinesweeperProblem
from Problem.cnf import *

class BruteForceSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)

    def isValid(self, assignment):
        # Calculate the heuristic by counting the number of violated clauses
        # We only calculate the heuristic for the model that we think is true
        model = set(assignment)
        model.update(-val for val in self.unknown_cells if val not in assignment)
        return not any(not CNFClause(clause).satisfy(model) for clause in self.cnf)

    def solve(self):
        n = len(self.unknown_cells) + 1
        for num_bombs in range(1, n):
            for combination in combinations(self.unknown_cells, num_bombs):
                if self.isValid(combination):
                    return combination
        return None

def solve_minesweeper_bruteforce(state):
    solver = BruteForceSolver(state)
    return solver.solve()
