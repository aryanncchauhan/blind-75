class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hash;
        for (int num : nums) {
            hash[num]++;
        }

        priority_queue<tuple<int, int>> pq;
        for (auto pair : hash) {
            pq.push({pair.second, pair.first});
        }

        vector<int> res;
        for (int i = 0; i < k; i++) {
            int curr = get<1>(pq.top());
            res.push_back(curr);
            pq.pop();
        }

        return res;
    }
};
