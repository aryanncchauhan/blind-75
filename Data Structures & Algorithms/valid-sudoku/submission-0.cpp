class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            unordered_set<char> row;
            int seen = 0;
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    seen++;
                    row.insert(board[i][j]);
                }
            }
            if (row.size() != seen) {
                return false;
            }
        }

        for (int i = 0; i < 9; i++) {
            unordered_set<char> column;
            int seen = 0;
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    seen++;
                    column.insert(board[j][i]);
                }
            }
            if (column.size() != seen) {
                return false;
            }
        }

        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                unordered_set<char> square;
                int seen = 0;
                for (int x = i; x < i + 3; x++) {
                    for (int y = j; y < j + 3; y++) {
                        if (board[x][y] != '.') {
                            seen++;
                            square.insert(board[x][y]);
                        }
                    }
                }
                if (square.size() != seen) {
                    return false;
                }
            }
        }

        return true;
    }
};
