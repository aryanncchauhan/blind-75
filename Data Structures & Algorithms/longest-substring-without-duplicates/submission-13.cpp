class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() < 2) return s.size();

        unordered_map<char, bool> hashmap;
        int l = 0;
        int r = 0;
        int res = 0;

        // maintain a window of valid substrings
        while (r < s.size()) {
            if (!hashmap[s[r]]) {
                hashmap[s[r]] = true;
            } else {
                while (s[l] != s[r]) {
                    hashmap[s[l]] = false;
                    l++;
                }
                l++;
            }
            res = max(res, r - l + 1);
            r++;
        }
        return res;
    }
};
