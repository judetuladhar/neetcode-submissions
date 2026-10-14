class Solution {
public:
    bool isAnagram(string s, string t) {
        return unordered_multiset<char>(s.begin(), s.end()) == unordered_multiset<char>(t.begin(), t.end());
    }
};
