from Problem.minesweeper_problem import MinesweeperProblem
from Problem.cnf import *

class BacktrackingSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)
    
    def count_valid_clauses(self, assignment):
        # Calculate the heuristic by counting the number of violated clauses
        # We only calculate the heuristic for the model that we think is true
        model = set(assignment)
        model.update(-val for val in self.unknown_cells if val not in assignment)
        valid_clause_count = sum(1 for clause in self.cnf if CNFClause(clause).satisfy(model))
        return valid_clause_count
    

    def solve(self, assignment, unknownCells, countValid=0):
        if countValid == len(self.cnf):
            return assignment

        unassigned = unknownCells - set(assignment)
        assign_removed = set()

        for assign in unassigned:
            assignment.append(assign)
            count = self.count_valid_clauses(assignment)
            if count > countValid:
                solution = self.solve(assignment, unknownCells, count)
                if solution:
                    return solution
                else:
                    unknownCells.remove(assign)
                    assign_removed.add(assign)
            else:
                unknownCells.remove(assign)
                assign_removed.add(assign)
            assignment.pop()

        unknownCells.update(assign_removed)
        return None

def solve_minesweeper_backtracking(state):
    solver = BacktrackingSolver(state)
    return solver.solve([], solver.unknown_cells.copy())