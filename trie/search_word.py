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
        cur_arr = [self.root]
        for c in word:
            index = ord(c) - ord('a')
            if c != '.':
                # print("searching word", c)
                for cur in cur_arr:
                    if cur.children[index] is not None:
                        cur_arr.append(cur.children[index])
                    cur_arr.pop(0)
            else:
                # print(". orson", len(cur_arr))
                new_arr = []
                for cur in cur_arr:
                    # print("forever",cur)
                    for i, child in enumerate(cur.children):
                        if child:
                            # print("i index set", i)
                            new_arr.append(child)

                    cur_arr.pop(0)
                cur_arr = new_arr

                # print(len(cur_arr))

        # print(cur_arr)

        for cur in cur_arr:
            if cur.isLeaf:
                return True
        return False

# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],  ["a"],[".at"],  ["bat"], [".at"],["an."],["a.d."],["b."],["a.d"],["."]]

# [null,null,null,null,null,false,false,null,true,true,false,false,true,false]


wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
print(wordDictionary.search("a"))
print(wordDictionary.search(".at"))
wordDictionary.addWord("bat")
print(wordDictionary.search(".at"))
print(wordDictionary.search("an."))
print(wordDictionary.search("a.d."))
print(wordDictionary.search("b."))
print(wordDictionary.search("a.d"))
print(wordDictionary.search("."))
# # print(wordDictionary)
# print(wordDictionary.search("day"))
# print(wordDictionary.search("bay"))
# print(wordDictionary.search("yaduu"))
# print(wordDictionary.search(".ay"))
# print(wordDictionary.search("b.."))
# print(wordDictionary.search(".."))
        
