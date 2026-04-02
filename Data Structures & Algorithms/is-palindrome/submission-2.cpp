class Solution {
public:
    bool isPalindrome(string s) {
        string ss;
        for (char c : s) {
            if (isalnum(c)) ss += tolower(c);
        }

        s = ss;

        int i = 0;
        int j = s.size() - 1;
        while (i <= j) {
            if (s[i] != s[j]) return false;
            i ++;
            j --;
        }
        
        return true;
    }
};
