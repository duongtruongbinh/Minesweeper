from pysat.solvers import Solver
from pysat.formula import CNF
from Problem.minesweeper_problem import MinesweeperProblem


class PYSATSolver(MinesweeperProblem):
    def __init__(self, state) -> None:
        super().__init__(state)
        self.preprocess()
        self.cnf = self.generate_cnf()

    def solve(self):
        cnf = CNF(from_clauses=self.cnf)

        with Solver(bootstrap_with=cnf) as solver:
            # Check if the formula is satisfiable
            if solver.solve(assumptions=[]):
                return solver.get_model()
            else:
                return None


def solve_minesweeper_pysat(state):
    solver = PYSATSolver(state)
    return solver.solve()
