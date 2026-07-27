class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for i in strs:
            x="".join(sorted(i))
            if x not in l:
                l[x]=[]
            l[x].append(i)
        return list(l.values())        