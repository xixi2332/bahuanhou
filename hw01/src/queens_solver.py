def solve_n_queens(n: int) -> list[list[int]]:
    """求解N皇后问题，返回所有合法的解"""
    solutions = []
    
    def backtrack(row, cols, diags1, diags2, path):
        if row == n:
            solutions.append(path.copy())
            return
        for col in range(n):
            if col not in cols and (row-col) not in diags1 and (row+col) not in diags2:
                cols.add(col)
                diags1.add(row-col)
                diags2.add(row+col)
                path.append(col)
                backtrack(row+1, cols, diags1, diags2, path)
                path.pop()
                diags2.remove(row+col)
                diags1.remove(row-col)
                cols.remove(col)
    
    backtrack(0, set(), set(), set(), [])
    return solutions

def print_board(solution: list[int], n: int) -> None:
    """可视化打印棋盘"""
    for row in range(n):
        line = ['.'] * n
        line[solution[row]] = 'Q'
        print(' '.join(line))
    print('-' * (2*n-1))

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"{n}皇后问题共有{len(solutions)}个解")
    print("第一个解的棋盘：")
    print_board(solutions[0], n)
