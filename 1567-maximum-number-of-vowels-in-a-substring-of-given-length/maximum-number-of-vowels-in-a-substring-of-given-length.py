class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        summ=0
        maxx=0
        summ=sum(1 for i in range(k) if s[i] in vowels )
        maxx=summ

        for i in range(k,len(s)):
            if s[i] in vowels:
                summ+=1
            if s[i-k] in vowels:
                summ-=1
            maxx=max(summ,maxx)
        return maxx           