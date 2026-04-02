class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<int>> rows;
        unordered_map<int, unordered_set<int>> cols;
        unordered_map<int, unordered_set<int>> squares;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                int cell = board[i][j] - 'a';

                if (rows[i].count(cell)) return false;
                else rows[i].insert(cell);

                if (cols[j].count(cell)) return false;
                else cols[j].insert(cell);

                int x = i / 3;
                int y = j / 3;
                int index = x * 3 + y;
                if (squares[index].count(cell)) return false;
                else squares[index].insert(cell);
            }
        }

        return true;
    }
};
