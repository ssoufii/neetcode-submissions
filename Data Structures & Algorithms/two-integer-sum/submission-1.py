class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      previous = {}  

      for i, n in enumerate(nums): #enumerate gives nums key value pairs we can utilize
        difference = target - n

        if difference in previous:
            return [previous[difference], i]

        previous[n] = i