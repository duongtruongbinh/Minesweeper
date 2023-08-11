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

# cnf_representation = solve_minesweeper_cnf(pro)
# print(cnf_representation)
