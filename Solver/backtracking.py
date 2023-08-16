from Problem.minesweeper_problem import MinesweeperProblem
from itertools import combinations
from Problem.cnf import *

class BacktrackingSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)

    def count_satisfied_clauses(self, assignment):
        # Calculate the heuristic by counting the number of violated clauses
        # We only calculate the heuristic for the model that we think is true
        model = set(assignment)
        model.update(-val for val in self.unknown_cells if val not in assignment)
        return sum(1 for clause in self.cnf if CNFClause(clause).satisfy(model))

    def solve(self, assignment, countSatifiedClauses=0):
        if countSatifiedClauses == len(self.cnf):
            return assignment

        unassigned = self.unknown_cells - set(assignment)

        for assign in unassigned:
            assignment.append(assign)
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