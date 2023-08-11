from itertools import combinations
from Problem.minesweeper_problem import MinesweeperProblem

class BruteForceSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)
        self.preprocess()
        
    def get_position(self, x, y):
        return x * self.cols + y + 1

    def is_combination_valid(self, combination):
        for i, j in self.known_cells.keys():
            neighbors = self.get_unknown_neighbors(i, j)
            num_bombs_around = self.known_cells[(i, j)]
            
            count = sum(1 for x, y in neighbors if self.get_position(x, y) in combination)
            
            if count != num_bombs_around:
                return False
        return True

    def solve(self):
        for num_bombs, _ in enumerate(self.unknown_cells, start=1):
            for combination in combinations(self.unknown_cells, num_bombs):
                if self.is_combination_valid(combination):
                    return combination  
        return None 

def solve_minesweeper_bruteforce(state):
    solver = BruteForceSolver(state)
    return solver.solve()
