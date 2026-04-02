class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

    def insert(self, word: str) -> None:
        def insertRecursion(root, i):
            letterIndex = ord(word[i]) - ord('a')

            if not root.children[letterIndex]:
                root.children[letterIndex] = PrefixTree()

            if i == len(word) - 1:
                root.children[letterIndex].isLeaf = True
            else:
                insertRecursion(root.children[letterIndex], i + 1)

        insertRecursion(self, 0)

    def search(self, word: str) -> bool:
        root = self

        for i, char in enumerate(word):
            letterIndex = ord(char) - ord('a')

            if i == len(word) - 1:
                return root.children[letterIndex] and root.children[letterIndex].isLeaf
            
            if not root.children[letterIndex]:
                return False
            
            root = root.children[letterIndex]
        
        return True

    def startsWith(self, prefix: str) -> bool:
        root = self

        for i, char in enumerate(prefix):
            letterIndex = ord(char) - ord('a')

            if not root.children[letterIndex]:
                return False

            root = root.children[letterIndex]

        return True
        
        