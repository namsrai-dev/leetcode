class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.isLeaf = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c != '.':

                index = ord(c) - ord('a')
                # print(index)
                # print(cur.children)
                if cur.children[index]:
                    return False
            cur = cur.children[index]
        return cur.isLeaf
            
        
