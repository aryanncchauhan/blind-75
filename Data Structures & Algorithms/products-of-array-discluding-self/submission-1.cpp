class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;

        int num_zeroes = 0;
        int product = 1;
        for (int n : nums) {
            if (n == 0) {
                num_zeroes++;
            } else {
                product *= n;
            }
        }

        for (int n : nums) {
            if (n != 0) {
                if (num_zeroes) res.push_back(0);
                else res.push_back(product / n);
            } else {
                if (num_zeroes > 1) res.push_back(0);
                else res.push_back(product);
            }
        }

        return res;
    }
};
