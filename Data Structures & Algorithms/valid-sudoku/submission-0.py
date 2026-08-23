class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in board:
            seen = set()

            for j in i:
                if j == ".":
                    continue

                if j in seen:
                    return False

                seen.add(j)

        for col in range(9):
            seen = set()

            for row in range(9):
                num = board[row][col]

                if num == ".":
                    continue
                
                if num in seen:
                    return False
                seen.add(num)

        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                square = (row // 3) * 3 + (col // 3)

                if num in boxes[square]:
                    return False
                boxes[square].add(num)

        return True
                
        