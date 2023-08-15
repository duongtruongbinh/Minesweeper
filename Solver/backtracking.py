from Problem.minesweeper_problem import MinesweeperProblem
from Problem.cnf import *


class BacktrackingSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)

    def complete_model(self, assignment):
        # Node stores the value of each cell that we think is true
        # Now we need to fill in the rest of the unknown_cells with false assumption
        model = set(assignment)
        model.update(-val for val in self.unknown_cells if val not in assignment)
        return sorted(model, key=abs)

    def count_satisfied_clauses(self, assignment):
        # Calculate the heuristic by counting the number of violated clauses
        # We only calculate the heuristic for the model that we think is true
        model = self.complete_model(assignment)
        return sum(1 for clause in self.cnf if CNFCLause(clause).satisfy(model))

    def solve(self, assignment, countSatifiedClauses=0):
        if countSatifiedClauses == len(self.cnf):
            return assignment

        unassigned = list(self.unknown_cells - set(assignment))

        while unassigned:
            assignment.append(unassigned.pop(0))
            count = self.count_satisfied_clauses(assignment)
            if count > countSatifiedClauses:
                solution = self.solve(assignment, count)
                if solution:
                    return solution
            assignment.pop()
        return None


def solve_minesweeper_backtracking(state):
    solver = BacktrackingSolver(state)
    return solver.solve([])
