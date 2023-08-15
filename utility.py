from Solver.pysat import solve_minesweeper_pysat
from Solver.astar import solve_minesweeper_astar
from Solver.bruteforce import solve_minesweeper_bruteforce
from Solver.backtracking import solve_minesweeper_backtracking
import time


def read_state(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    return [list(map(int, line.strip().split(","))) for line in lines]


def output_solution(model, problem):
    with open("Project_2/output.txt", "w") as fout:
        if model is None:
            fout.write("No solution")
            return

        for assignment in model:
            if assignment > 0:
                i = (assignment - 1) // len(problem[0])
                j = (assignment - 1) % len(problem[0])
                problem[i][j] = -1

        for row in problem:
            fout.write(",".join(map(lambda x: "*" if x == -1 else str(x), row)))
            fout.write("\n")


def main_function():
    print("Choose the algorithm:")
    print("1. Brute force")
    print("2. Backtracking")
    print("3. SAT")
    print("4. A*")

    algorithm_tostr = ["Brute force", "Backtracking", "SAT", "A*"]
    algorithm = int(input("Enter the number of the algorithm: "))
    file_name = input("Enter the file name or path: ")
    state = read_state(file_name)
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

    print("Algorithm: " + algorithm_tostr[algorithm - 1])
    print("Time: " + str(time_end - time_start))

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
