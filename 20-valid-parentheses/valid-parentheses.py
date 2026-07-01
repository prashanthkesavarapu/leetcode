from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        pairs={')':'(',']':'[','}':'{'}
        opening=set(pairs.values())
        balance=True

        for i in s:
            if i in opening:
                stack.append(i)
            elif i in pairs:
                if not stack or stack.pop()!=pairs[i]:
                    balance= False
        if balance and len(stack)==0:
            return True                
        else:
            return False    

        