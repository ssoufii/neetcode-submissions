class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs: #loop through each word in the list
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s): #while i is in bounds

            j = i #set a pointer j to i that will go till #
            
            while s[j] != "#":
                j +=1
            length = int(s[i:j]) #first number of encoded string which represents its length 
            #we've now found a #

            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
