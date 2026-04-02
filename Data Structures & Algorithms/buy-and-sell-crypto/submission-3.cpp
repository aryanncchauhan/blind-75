class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // precompute the smallest value to the left of each index
        int leftMin[100];
        leftMin[0] = prices[0];
        int currMin = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            leftMin[i] = currMin;
            currMin = min(currMin, prices[i]);
        }
        
        // find largest difference
        int res = 0;
        for (int i = 0; i < prices.size(); i++) {
            res = max(res, prices[i] - leftMin[i]);
        }
        return res;
    }
};
