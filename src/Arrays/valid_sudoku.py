def isValidSudoku(board: list[list[str]]) -> bool:
    # HELPER FUNCTIONS
    def checkList(l):
        seen = set()
        for cell in l:
            if cell == '.':
                continue

            if cell in seen:
                return False

            seen.add(cell)

        return True

    def checkSubSquare(board, subSquareStart: tuple):
        startRow, startColumn = subSquareStart
        seen = set()

        for i in range(startRow, startRow + 3):
            for j in range(startColumn, startColumn + 3):
                cell = board[i][j]

                if cell == '.':
                    continue

                if cell in seen:
                    return False

                seen.add(cell)

        return True

    # SOLUTION

    # check rows
    for i in range(9):
        row = board[i]
        validity = checkList(row)
        if not validity:
            return False

    # check columns
    for j in range(9):
        column = [board[i][j] for i in range(9)]
        validity = checkList(column)
        if not validity:
            return False

    # check subsquares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            validity = checkSubSquare(board, (i, j))
            if not validity:
                return False

    # else board passes all checks
    return True

if __name__ == "__main__":
    test_board =[
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    test_expected = True

    output = isValidSudoku(test_board)
    if output is not test_expected:
        print("Test case failed.")