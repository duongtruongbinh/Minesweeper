def read_state(filename):
    with open(f"testcases/{filename}", "r") as f:
        lines = f.readlines()

    return [[int(cell[0]) for cell in line.split(" ")] for line in lines]


def output_solution(solution, state, size):
    with open(f"testcases/output_{size}x{size}.txt", "w") as fout:
        if solution:
            print("Solution found:")
            for assignment in solution:
                if assignment > 0:
                    i = (assignment - 1) // len(state[0])
                    j = (assignment - 1) % len(state[0])
                    state[i][j] = -1

            for row in state:
                print(",".join(map(lambda x: "*" if x == -1 else str(x), row)))
                fout.write(
                    ",".join(map(lambda x: "*" if x == -1 else str(x), row)))
            print()
            fout.write("\n")
        else:
            print('No solution')
            fout.write("No solution")
