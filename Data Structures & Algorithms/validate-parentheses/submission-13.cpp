class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> hash = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        stack<char> stk;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                stk.push(c);
            } else {
                if (stk.empty()) return false;
                char lastBracket = stk.top();
                stk.pop();
                if (c != hash[lastBracket]) return false;
            }
        }
        return stk.empty();
    }
};
