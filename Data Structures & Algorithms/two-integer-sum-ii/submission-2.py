class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(0,len(numbers)):
            rem = target - numbers[i]

            if rem in hashMap:
                return sorted([hashMap.get(rem),i+1])
            hashMap[numbers[i]] = i+1
        
        return []