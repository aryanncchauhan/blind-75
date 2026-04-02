class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // initialse result variable
        vector<vector<int>> res;

        // sort input
        sort(nums.begin(), nums.end());

        int n = nums.size();
        for (int i = 0; i < n; i++) {
            // reduce to two sum
            vector<int> temp;
            for (int j = i + 1; j < n; j++) {
                temp.push_back(nums[j]);
            }

            if (temp.size() < 2) continue;

            int target = 0 - nums[i];
            int l = 0;
            int r = temp.size() - 1;
            while (l < r) {
                int sum = temp[l] + temp[r];

                if (sum == target) {
                    vector<int> entry = {temp[l], temp[r], nums[i]};
                    sort(entry.begin(), entry.end());
                    res.push_back(entry);
                    r--;
                    l++;
                    continue;
                } 
                else if (sum > target) r--;
                else l++;
            }
        }
        sort(res.begin(), res.end());
        res.erase(unique(res.begin(), res.end()), res.end());
        return res;
    }
};
