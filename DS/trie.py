class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def __repr__(self):
        return f"Children : {self.children}"

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, item):
        curr = self.root
        for c in item:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    
    def search(self, query):
        curr = self.root
        for c in query:
            if c not in curr.children:
                print("char not found", c)
                return False
            curr = curr.children[c]
        return curr.endOfWord
    def startsWith(self, query):
        curr = self.root
        words = []
        prefix = ""
        for c in query:
            if c not in curr.children:
                return (False, words) # DO FUzzy Logic HEre
            curr = curr.children[c]
            prefix += c
        self.dfs(curr, prefix, words)
        return (True, words)

        return (hasWord, words)

    def dfs(self, node, prefix, words):
        if node.endOfWord:
            words.append(prefix)
        for char, child in node.children.items():
            self.dfs(child, prefix + char, words)

    def startsWithCount(self, query, k):
        curr = self.root
        words = []
        prefix = ""
        for c in query:
            if c not in curr.children:
                return []
            curr = curr.children[c]
            prefix += c
        self.dfsWithCount(curr, prefix, words, k)
        return words[:k]

    def dfsWithCount(self, node, prefix, words, k):
        if len(words) >= k:
            return
        if node.endOfWord:
            words.append(prefix)
        for char, child in node.children.items():
            self.dfsWithCount(child, prefix + char, words, k)

if __name__ == "__main__":
    trie = Trie()

    words = [
    "apple", "application", "app", "banana", "basket", "bat", "ball", "car",
    "cat", "camel", "dog", "elephant", "egg", "fish", "fox", "grape", "goat",
    "hat", "horse", "ice", "ink", "jam", "jelly", "kite", "king", "lion",
    "lemon", "mango", "monkey", "nest", "nut", "ostrich", "orange", "owl",
    "peach", "pear", "plum", "quail", "queen", "rabbit", "rope", "rose",
    "snake", "tiger", "umbrella", "unicorn", "vase", "violin", "wagon", "whale",
    "xylophone", "yak", "zebra", "applepie", "book", "computer", "desk", "dolphin",
    "elephantear", "fridge", "giraffe", "hammer", "icecream", "jacket", "kangaroo",
    "leopard", "muffin", "notebook", "ocean", "penguin", "quilt", "raccoon",
    "shark", "taco", "unicornio", "violinist", "watermelon", "xylophonist", "yogurt",
    "zeppelin", "ant", "bird", "caterpillar", "dragon", "elephantseal", "frog",
    "giraffehead", "hippo", "iguana", "jellyfish", "koala", "lemur", "mosquito",
    "newt", "octopus", "panda", "quokka", "rhinoceros", "snail", "turtle",
    "unicornfish", "vulture", "whalewhale", "xenops", "yakface", "zebrafish", "apple", "application", "appetizer", "baking", "basketball", "bathtub", "catastrophe",
    "caterpillar", "doghouse", "doggy", "dogwood", "elephantine", "fisherman", "fishing",
    "jellybean", "jellyfish", "kiteboarding", "kitesurfing", "lemonade", "lemonlime",
    "orangutan", "orangejuice", "orangetree", "applesauce", "bananaapple", "catapult",
    "dogbone", "dogcatcher", "dogged", "elephantiasis", "fishbowl", "fishhook", "jellyroll",
    "jellydonut", "kiteflyer", "lemonzest", "orangegrove"
    ]
    for word in words:
        trie.insert(word)
    queries = [
    "app", "banana", "cat", "dog", "elephant", "fish", "jelly", "kite", "lemon", "orange"
    ]

    results = {}
    for q in queries:
        results[q] = trie.startsWith(q)

    print(results)