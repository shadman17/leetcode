class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Initialize Trie
trie = Trie()

# Insert some words
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("band")

# Search for complete words
print(trie.search("apple"))   # Expected: True
print(trie.search("app"))     # Expected: True
print(trie.search("appl"))    # Expected: False
print(trie.search("banana"))  # Expected: True
print(trie.search("ban"))     # Expected: False

# Check for prefixes
print(trie.startsWith("app")) # Expected: True
print(trie.startsWith("ban")) # Expected: True
print(trie.startsWith("bat")) # Expected: False
