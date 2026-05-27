class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for duplicates in row
        for row in board:
            duplicate_row = set()
            for individual in row:
                if individual == ".":
                    continue
                else:
                    if individual in duplicate_row:
                        return False
                    else:
                        duplicate_row.add(individual)
        
        # Check for duplicates in column
        for i in range(9):
            duplicate_column = set()
            for row in board:
                if row[i] == ".":
                    continue
                else:
                    if row[i] in duplicate_column:
                        return False
                    else:
                        duplicate_column.add(row[i])
    
        # Check for 3x3
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                duplicate_square = set()

                for i in range(3):
                    for j in range(3):
                        value = board[row + i][col + j]

                        if value == ".":
                            continue

                        if value in duplicate_square:
                            return False

                        duplicate_square.add(value)

        print(duplicate_row)
        print(duplicate_column)
        return True