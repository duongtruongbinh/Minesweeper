import utility
from Solver.pysat import solve_minesweeper_pysat
from Solver.astar import solve_minesweeper_astar
from Solver.bruteforce import solve_minesweeper_bruteforce
from Solver.backtracking import solve_minesweeper_backtracking


if __name__ == "__main__":

    print("Choose the algorithm:")
    print("1. Brute force")
    print("2. Backtracking")
    print("3. SAT")
    print("4. A*")

    algorithm = int(input("Enter the number of the algorithm: "))
    state = utility.read_state("testcases/3x3.txt")
    print("Input: ")

    for row in state:
        print(",".join(map(str, row)))
    print()

    if algorithm == 1:
        solution = solve_minesweeper_bruteforce(state)
    elif algorithm == 2:
        solution = solve_minesweeper_backtracking(state)
    elif algorithm == 3:
        solution = solve_minesweeper_pysat(state)
    elif algorithm == 4:
        solution = solve_minesweeper_astar(state)

    if solution:
        print("Solution found")
        for assignment in solution:
            if assignment > 0:
                i = (assignment - 1) // len(state[0])
                j = (assignment - 1) % len(state[0])
                state[i][j] = -1

        for row in state:
            print(",".join(map(lambda x: "*" if x == -1 else str(x), row)))
        print()

    else:
        print('No solution')
