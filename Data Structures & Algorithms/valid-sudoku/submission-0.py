class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check Columns
        for j in range(9):
            seen = [False] * 9
            for i in range(9):
                if(board[i][j] == "."):
                    continue
                if seen[ord(board[i][j]) - ord("1")]:
                    print(f"col: {j}")
                    return False
                else:
                    seen[ord(board[i][j]) - ord("1")] = True
        #check rows
        for i in range(9):
            seen = [False] * 9
            for j in range(9):
                if(board[i][j] == "."):
                    continue
                if seen[ord(board[i][j]) - ord("1")]:
                    print(f"row: {i}")
                    return False
                else:
                    seen[ord(board[i][j]) - ord("1")] = True
        #check 3x3
        for step in range(9):
            #step i start = step/3 j start = step%3
            seen = [False] * 9
            i_start = int(step/3) * 3
            j_start = int(step%3) * 3
            for dx in range(3):
                for dy in range(3):
                    if(board[i_start+dx][j_start+dy] == "."):
                        continue
                    if seen[ord(board[i_start+dx][j_start+dy]) - ord("1")]:
                        print(f"box: {step} pos {i_start+dx} {j_start+dy}")
                        return False
                    else:
                        seen[ord(board[i_start+dx][j_start+dy]) - ord("1")] = True
        return True
