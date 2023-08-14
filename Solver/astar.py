from Problem.minesweeper_problem import MinesweeperProblem
from Problem.cnf import *
import heapq

class AStarSolver(MinesweeperProblem):
    def __init__(self, state):
        super().__init__(state)
        
        self.frontier = []
        self.frontier.append((1, []))
        self.explored = set()

    def to_string(self, node):
        # Convert node to string for storing in explored set
        node_str = ' '.join(map(str, sorted(node, key=abs)))
        return node_str

    def complete_model(self, node: list):
        # Node stores the value of each cell that we think is true
        # Now we need to fill in the rest of the unknown_cells with false assumption
        model = set(node)
        model.update(-val for val in self.unknown_cells if val not in node)
        return sorted(model, key=abs)

    def heuristic(self, node):
        # Calculate the heuristic by counting the number of violated clauses
        # We only calculate the heuristic for the model that we think is true
        model = self.complete_model(node)
        violated_clause_count = sum(1 for clause in self.cnf if not OR(clause).satisfy(model))
        return violated_clause_count

    def expand_node(self, node):
        # Generate children by adding one more variable to the node
        marked = set(node)
        children = [node + [val] for val in self.unknown_cells if val not in marked]
        return children

    def solve(self):
        while self.frontier:
            cost, node = heapq.heappop(self.frontier)

            heuristic = self.heuristic(node)
            cost -= heuristic

            if heuristic == 0:
                return node

            self.explored.add(self.to_string(node))

            for child in self.expand_node(node):
                child_string = self.to_string(child)
                if child_string not in self.explored:
                    self.frontier.append((self.heuristic(child) + cost + 1, child))

            heapq.heapify(self.frontier)
        return None

def solve_minesweeper_astar(state):
    solver = AStarSolver(state)
    return solver.solve()