class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l="".join(map(str,digits))
        e=int(l)
        e=e+1
        w=[int(i) for i in str(e)]
        return w

