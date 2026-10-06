class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for idx, number in enumerate(numbers,start=1):
            if target-number in seen:
                return [seen[target-number], idx]
            else:
                seen[number]=idx