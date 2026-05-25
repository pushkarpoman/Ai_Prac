def is_safe(queens, row, col):
    for c in range(col):
        if queens[c] == row or abs(queens[c] - row) == abs(c - col):
            return False
    return True

def solve_n_queens_util(queens, col, n):
    if col == n:
        return True
    for row in range(n):
        if is_safe(queens, row, col):
            queens[col] = row
            if solve_n_queens_util(queens, col + 1, n):
                return True
    return False

def print_solution(queens):
    n = len(queens)
    for r in range(n):
        for c in range(n):
            if queens[c] == r:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

n = int(input("Enter value of N: "))
queens = [-1] * n
found = solve_n_queens_util(queens, 0, n)

if found:
    print(f"Found a solution for {n}-Queens problem:")
    print_solution(queens)
else:
    print("Solution does not exist")
