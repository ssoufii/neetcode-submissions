class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        empty_map = defaultdict(list)
        for s in strs: #for every word in the list
            count = [0] * 26 #creates a 26 index long list of zeros, refreshes for each new word
            for c in s: #for every character in s:
                count[ord(c) - ord('a')] +=1 #find alphabet index of c, and increment its count by one in the list
            
            empty_map[tuple(count)].append(s) #groups each new s with all other S's that have the same letter count frequencies

        return list(empty_map.values())