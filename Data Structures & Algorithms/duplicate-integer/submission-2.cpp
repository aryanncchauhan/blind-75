class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> hash;
        for (int num : nums) {
            if (hash.find(num) != hash.end()) return true;
            else hash[num]++;
        }
        return false;
    }
};
