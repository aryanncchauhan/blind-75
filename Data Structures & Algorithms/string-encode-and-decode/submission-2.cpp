class Solution {
public:

    string encode(vector<string>& strs) {
        vector<int> sizes;
        for (string s : strs) {
            sizes.push_back(s.size());
        }

        string res = "";
        for (int i = 0; i < strs.size(); i++) {
            res += to_string(sizes[i]);
            res += "#";
            res += strs[i];
        }

        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;

        int i = 0; 
        while (i < s.size()) {
            string s_length;
            
            while (s[i] != '#') {
                s_length += s[i];
                i++;
            }

            int i_length = stoi(s_length);
            i++;

            string curr = s.substr(i, i_length);
            res.push_back(curr);

            i += i_length;
        }

        return res;
    }
};
