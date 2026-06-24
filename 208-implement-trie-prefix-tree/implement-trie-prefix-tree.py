class Trie:

    def __init__(self):
        self.root={}
        

    def insert(self, word: str) -> None:
        d=self.root
        for ch in word:
            d=d.setdefault(ch,{})
        d["*"]=True    

    def search(self, word: str) -> bool:
        d=self.root

        for ch in word:
            if ch not in d:
                return False
            d=d[ch] 
        return "*" in d       
        

    def startsWith(self, prefix: str) -> bool:
        d=self.root

        for ch in prefix:
            if ch not in d:
                return False
            d=d[ch] 
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)