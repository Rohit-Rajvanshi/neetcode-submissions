class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = tmp_count = 0
        for i in nums:
            if i == 1 :
                tmp_count += 1
                count = max(count, tmp_count)
            else: 
                tmp_count = 0
        return count 


        