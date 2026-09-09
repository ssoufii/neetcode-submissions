class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):

            return False

        hash_s = {} #counts each characters count
        hash_t = {} #use dictionarys because sets dont have keys


        # building the hashmap
        for i in range(len(s)): #1,2,3...len(s)
            #hash_s[s[i]] is hash_s[a_letter] and will hold a letters count
            hash_s[s[i]] = 1 + hash_s.get(s[i],0)
            hash_t[t[i]] = 1 + hash_t.get(t[i],0)

        #once we have a letters count, we iterate thru the hash counter and
        #ensure the counter for each letter is the same, else return false
        for count in hash_s:
            if hash_s.get(count,0) != hash_t.get(count, 0):
                return False

        else: return True
        


            
        