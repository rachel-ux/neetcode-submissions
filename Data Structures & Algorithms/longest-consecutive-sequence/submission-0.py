class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0
        for i in numSet:
            if i - 1 in numSet:
                continue
            else:
                current = i
                depth = 1
                while current + 1 in numSet:
                    current+=1
                    depth += 1
            
            max_length = max(max_length,depth)
        return max_length