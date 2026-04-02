class Solution {
public:
    int findMin(vector<int> &nums) {
        int res = nums[0];
        int lo = 0;
        int hi = nums.size() - 1;
        int mid = 0;
        while (lo <= hi) {
            if (nums[lo] < nums[hi]) {
                res = min(res, nums[lo]);
                break;
            }

            mid = (lo + hi) / 2;
            res = min(res, nums[mid]);
            if (nums[mid] >= nums[lo]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return res;
    }
};
