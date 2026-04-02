class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hashset(nums.begin(), nums.end());
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (hashset.find(nums[i] - 1) == hashset.end()) {
                int length = 0;
                int curr = nums[i];
                while (hashset.find(curr) != hashset.end()) {
                    length++;
                    curr++;
                }
                res = max(res, length);
            }
        }
        return res;
    }
};
