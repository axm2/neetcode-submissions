class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            k = tuple(sorted(s))
            if k in h:
                h[k] += [s]
            else:
                h[k] = [s]
        return list(h.values())