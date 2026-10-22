class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node["$"] = True 


    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if(i not in node):
                return False
            node = node[i]

        return "$" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node:
                return False
            node = node[i]
            
        return True
        