class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()
        lptr = 0
        rptr = len(clean) - 1

        while lptr < rptr:
            if clean[lptr] != clean[rptr]:
                return False
            lptr+=1
            rptr-=1

        return True
