class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurence = 0
        length = len(nums)
        for num in nums[:]: 
            if num == val:
                occurence += 1
                nums.remove(num)
        return length - occurence 
