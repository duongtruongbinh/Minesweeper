from itertools import combinations


class MinesweeperProblem:
    def __init__(self, state):
        self.known_cells = dict()
        self.unknown_cells = set()
        self.state = state
        self.rows, self.cols = len(state), len(state[0])

    def preprocess(self):
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.state[i][j]

                if not 0 <= value <= 8:
                    raise ValueError("Invalid input")

                if value > 0:
                    self.known_cells[(i, j)] = value
                    # Check if the number of bombs in neighbors and the number of unknown neighbors is valid
                    self.check_valid_neighbors(i, j)
                else:
                    self.unknown_cells.add(i * self.cols + j + 1)

    def check_valid_neighbors(self, i, j):
        neighbors = self.get_unknown_neighbors(i, j)
        num_unknown_neighbors = sum([
            1 for x, y in neighbors if self.state[x][y] == 0])

        # Check if the number of unknown neighbors is less than the number of bombs
        # If it is, then the input is invalid
        if num_unknown_neighbors < self.known_cells[(i, j)]:
            raise ValueError("Invalid input")

    def get_unknown_neighbors(self, i, j):
        i_range = range(max(0, i - 1), min(i + 2, self.rows))
        j_range = range(max(0, j - 1), min(j + 2, self.cols))

        # Neighbors are all cells that are not the cell itself, not known and not out of bound
        neighbors = [(x, y) for x in i_range for y in j_range if (
            x, y) != (i, j) and (x, y) not in self.known_cells]

        return neighbors

    def generate_cnf(self):
        cnf_clauses = []
        # Known cell's value is the number of bombs in its neighbors
        # A cell is true if it is a bomb, false if it is not
        # Example: 2 bombs in 5 neighbors {1,2,3,4,5}
        # CNF clauses: There is exactly 2 bombs in 5 neighbors
        # We will combine 2 clauses: At least 2 bombs in 5 neighbors and at most 2 bombs in 5 neighbors
        # At least 2 bombs in 5 neighbors: [[1,2,3,4], [1,2,3,5], [1,2,4,5], [1,3,4,5], [2,3,4,5]]
        # At most 2 bombs in 5 neighbors: [[-1,-2,-3], [-1,-2,-4], [-1,-3,-4], [-2,-3,-4]]
        # => CNF clauses: [[1,2,3,4], [1,2,3,5], [1,2,4,5], [1,3,4,5], [2,3,4,5], [-1,-2,-3], [-1,-2,-4], [-1,-3,-4], [-2,-3,-4]]
        # generally: At least k bombs in n neighbors: C(n,n-k+1) and at most k bombs in n neighbors: C(n,k+1)
        for i, j in self.known_cells.keys():
            neighbors = self.get_unknown_neighbors(i, j)

            # Generate CNF clauses for at least k bombs in n neighbors
            for combination in combinations(neighbors, len(neighbors) - self.known_cells[(i, j)] + 1):
                positive_clause = [x * self.cols +
                                   y + 1 for x, y in combination]
                cnf_clauses.append(positive_clause)

            # Generate CNF clauses for at most k bombs in n neighbors
            for combination in combinations(neighbors, self.known_cells[(i, j)] + 1):
                negative_clause = [-(x * self.cols + y + 1)
                                   for x, y in combination]
                cnf_clauses.append(negative_clause)

        # Return unique clauses
        return list(set(map(tuple, cnf_clauses)))
