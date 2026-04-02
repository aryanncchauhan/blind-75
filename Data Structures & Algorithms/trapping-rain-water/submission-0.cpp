class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0;

        int currMaxLeft = 0;
        int maxLeft[1000];
        int maxRight[1000];

        maxLeft[0] = 0;
        for (int i = 1; i < height.size(); i++) {
            currMaxLeft = max(currMaxLeft, height[i - 1]);
            maxLeft[i] = currMaxLeft;
        }

        int currMaxRight = 0;
        maxRight[height.size() - 1] = 0;
        for (int i = height.size() - 2; i >= 0; i--) {
            currMaxRight = max(currMaxRight, height[i + 1]);
            maxRight[i] = currMaxRight;
        }

        for (int i = 0; i < height.size(); i++) {
            int water = min(maxLeft[i], maxRight[i]) - height[i];
            if (water > 0) res += water;
        }

        return res;
    }
};
