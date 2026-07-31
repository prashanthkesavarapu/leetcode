from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        c=Counter(word)
    
        sor=sorted(c.values(), reverse=True)

        total_pushes=0

        for i , v in enumerate(sor):
            push=(i//8)+1
            total_pushes+=v*push
        return total_pushes    