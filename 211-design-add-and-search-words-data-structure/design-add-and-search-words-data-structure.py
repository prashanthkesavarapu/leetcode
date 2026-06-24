class WordDictionary:

    def __init__(self):
        self.root={}
        

    def addWord(self, word: str) -> None:
        d=self.root
        for ch in word:
            d=d.setdefault(ch,{})
        d["*"]=True    
        

    def search(self, word: str) -> bool:
        def dfs(j,d):
            for i in range(j,len(word)):
                ch=word[i]

                if ch==".":
                    for k in d:

                        if k!="*" and dfs(i+1,d[k]):
                            return True
                    return False
                else:
                    if ch not in d:
                        return False
                    d=d[ch]
            return "*" in d
        return dfs(0,self.root)                         
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)