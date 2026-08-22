class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stk = []
        for c in s:
            if c in pairs and len(stk)>0 and stk[-1]==pairs[c]:
                stk.pop()
            else:
                stk.append(c)
        return len(stk)==0
