def valid_solution(board):
    length = len(board)
    for row in range(length):
        valid_cells = set()
        # check rows
        if 0 in board[row] or len(set(board[row])) < 9:
            return False
        #check col
        for col in range(length):
            if board[col][row] in valid_cells:
                return False
            valid_cells.add(board[col][row])
    # Check regions
    for n in range(0, length, 3):
        valid_cells = set()
        for row in range(n, n+3):
            for col in range(n, n+3):
                if board[row][col] not in valid_cells:
                    valid_cells.add(board[row][col])
                else:
                    return False
    return True

correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def validSolution(board):
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False
    
    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return False
    
    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]
            
            if sorted(region) != correct:
                return False
    
    # if everything correct
    return True


print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9]]))