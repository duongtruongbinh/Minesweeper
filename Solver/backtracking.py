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
        return sum(1 for clause in self.cnf if CNFClause(clause).satisfy(model))

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

# def get_position(self, x, y):
    #     return x * self.cols + y + 1

    # def is_combination_valid(self, combination):
    #     for i, j in self.known_cells.keys():
    #         neighbors = self.get_unknown_neighbors(i, j)
    #         num_bombs_around = self.known_cells[(i, j)]

    #         count = sum(1 for x, y in neighbors if self.get_position(
    #             x, y) in combination)

    #         if count != num_bombs_around:
    #             return False
    #     return True

    # def check_subproblem(self, combination, i, j, value):
    #     neighbors = self.get_unknown_neighbors(i, j)
    #     count = sum([1 for x, y in combination if (x, y) in neighbors])
    #     return count == value

    # def check_combination(self):
    #     self.solution = [self.get_position(i, j) for i in range(
    #         self.rows) for j in range(self.cols) if self.state[i][j] == -1]
    #     return self.is_combination_valid(self.solution)
    # def assign_combination(self, combination):
    #     for neighbor in combination:
    #         self.state[neighbor[0]][neighbor[1]] = -1

    # def unassign_combination(self, combination):
    #     for neighbor in combination:
    #         self.state[neighbor[0]][neighbor[1]] = 0


def solve_minesweeper_backtracking(state):
    solver = BacktrackingSolver(state)
    return solver.solve([])
