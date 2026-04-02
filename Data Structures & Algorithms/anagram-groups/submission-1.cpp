class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash;
        vector<vector<string>> res; 

        for (string s : strs) {
            string original = s;
            string sorted = s;
            sort(sorted.begin(), sorted.end());

            hash[sorted].push_back(original);
        }

        for (auto pair : hash) {
            vector<string> list;
            for (auto s : pair.second) {
                list.push_back(s);
            }
            res.push_back(list);
        }

        return res;
    }
};
