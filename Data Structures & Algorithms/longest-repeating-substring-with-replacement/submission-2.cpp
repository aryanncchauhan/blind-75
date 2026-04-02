class Solution {
public:
    int characterReplacement(string s, int k) {
        if (s.size() < 2) return s.size();

        int res = 0;

        int len = s.size();
        unordered_map<char, int> hashmap;
        int l = 0;
        for (int r = 0; r < len; r++) {
            hashmap[s[r]]++;
            while (getWinSize(l, r) - getMostFrequentChar(hashmap) > k) {
                hashmap[s[l]]--;
                l++;
            }
            res = max(res, getWinSize(l, r));
        }
        
        return res;
    }
private:
    int getWinSize(int l, int r) {
        return r - l + 1;
    }

    int getMostFrequentChar(unordered_map<char, int> hashmap) {
        int res = 0;
        for (char i = 'A'; i <= 'Z'; i++) {
            res = max(res, hashmap[i]);
        }
        return res;
    }
};
