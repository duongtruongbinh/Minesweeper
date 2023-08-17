import utility
from Solver.pysat import solve_minesweeper_pysat
from Solver.astar import solve_minesweeper_astar
from Solver.bruteforce import solve_minesweeper_bruteforce
from Solver.backtracking import solve_minesweeper_backtracking
import time

if __name__ == "__main__":

    print("Choose the algorithm:")
    print("1. Brute force")
    print("2. Backtracking")
    print("3. SAT")
    print("4. A*")

    algorithm = int(input("Enter the number of the algorithm: "))
    filename = input("File test case input: ")
    state = utility.read_state(filename)
    size = len(state)
    print("Input: ")

    for row in state:
        print(",".join(map(str, row)))
    print()

    time_start = time.time()

    if algorithm == 1:
        solution = solve_minesweeper_bruteforce(state)
    elif algorithm == 2:
        solution = solve_minesweeper_backtracking(state)
    elif algorithm == 3:
        solution = solve_minesweeper_pysat(state)
    elif algorithm == 4:
        solution = solve_minesweeper_astar(state)

    time_end = time.time()

    print(f"Time: {(time_end - time_start):0.9f}s")

    utility.output_solution(solution, state, size)
