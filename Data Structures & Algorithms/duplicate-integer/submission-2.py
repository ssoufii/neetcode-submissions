class Solution:
    def hasDuplicate(self, nums):
        hash_map = []

        for i in nums: 
            if i in hash_map:
                return True

            else: 

                hash_map.append(i)


        return False

            
            
        