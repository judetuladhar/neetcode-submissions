class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        mostRecent = {}
        l = 0
        r = 1

        if not s:
            return 0
        else:
            mostRecent[s[l]] = l
            longest += 1

        while r < len(s):
            if s[r] in mostRecent and mostRecent.get(s[r]) >= l:
                l = mostRecent.get(s[r]) + 1
            mostRecent[s[r]] = r
            r += 1
            longest = max(longest, r - l)

        return longest


