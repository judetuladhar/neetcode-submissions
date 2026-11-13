class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            newstr = strs[i]
            encoded_string = encoded_string + str(len(strs[i])) + "#" + newstr
        return encoded_string
        


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        empty = ""
        while s != empty:
            wlen = int(s[:s.find("#")])
            decoded_strs.append(s[s.find("#")+1:s.find("#")+1+wlen])
            s = s[s.find("#")+1+wlen:]
        return decoded_strs
