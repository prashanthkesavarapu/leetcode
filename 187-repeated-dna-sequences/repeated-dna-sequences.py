class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        repeated=set()
        for i in range(len(s)):
            ss=s[i:i+10]  
            if ss in seen:
                repeated.add(ss)
            else:
                seen.add(ss)
        return list(repeated)            


                

        