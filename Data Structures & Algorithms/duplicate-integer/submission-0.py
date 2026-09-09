class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_t = set()

        for i in nums: 
            if i in hash_t: 
                return True

            else:
                hash_t.add(i) 

        return False
            
        