"""
A Trie is a special data structure used to store strings that can be visualized like a graph. It consists of nodes and edges. 
Each node consists of at max 26 children and edges connect each parent node to its children. 
These 26 pointers are nothing but pointers for each of the 26 letters of the English alphabet A separate edge is maintained for every edge.
Strings are stored in a top to bottom manner on the basis of their prefix in a trie. All prefixes of length 1 are stored at until level 1, 
all prefixes of length 2 are sorted at until level 2 and so on.
Now, one would be wondering why to use a data structure such as a trie for processing a single string? Actually, Tries are generally used on groups of strings, 
rather than a single string. When given multiple strings , we can solve a variety of problems based on them. For example, consider an English dictionary and a 
single string , find the prefix of maximum length from the dictionary strings matching the string . Solving this problem using a naive approach would require us 
to match the prefix of the given string with the prefix of every other word in the dictionary and note the maximum. The is an expensive process considering the 
amount of time it would take. Tries can solve this problem in much more efficient way.
Before processing each Query of the type where we need to search the length of the longest prefix, we first need to add all the existing words into the dictionary. 
A Trie consists of a special node called the root node. This node doesn't have any incoming edges. It only contains 26 outgoing edfes for each letter in the 
alphabet and is the root of the Trie.
So, the insertion of any string into a Trie starts from the root node. All prefixes of length one are direct children of the root node. 
In addition, all prefixes of length 2 become children of the nodes existing at level one.
"""
class Trie:

    def __init__(self):
        self.dic = {}

    def insert(self, word):
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['end'] = {}

    def search(self, word):
        cur = self.dic
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False
        if 'end' in cur:
            return True
        return False
        

    def startsWith(self, prefix):
        cur = self.dic
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True

obj = Trie() # Creating object of Trie Class
obj.insert("hello") # Insert "hello" into Trie
obj.insert("hi") # Insert "hi" into Trie
obj.insert("hey") # Insert "hey" into Trie
print(obj.search("hi")) # return True
print(obj.startsWith("he")) # return True
print(obj.startsWith("heyy")) # return False