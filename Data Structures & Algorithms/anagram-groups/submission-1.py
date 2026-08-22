class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            if tuple(sorted(s)) in h:
                h[tuple(sorted(s))] += [s]
            else:
                h[tuple(sorted(s))] = [s]
        return list(h.values())