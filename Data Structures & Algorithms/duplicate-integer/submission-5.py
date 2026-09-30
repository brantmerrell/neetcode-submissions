class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        my_set = {}
        for num in nums:
            if len(my_set)>0 and num in my_set.keys():
                return True
            else:
                my_set[num] = 1
        return False