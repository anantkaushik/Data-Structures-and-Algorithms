"""
Pattern searching is an important problem in computer science. When we do search for a string in notepad/word file or 
browser or database, pattern searching algorithms are used to show the search results.

The KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than once in 
the pattern) of the pattern and improves the worst case complexity to O(n). The basic idea behind KMP’s algorithm is: 
whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. 
We take advantage of this information to avoid matching the characters that we know will anyway match. 
"""
def shiftTable(s):
    shiftT = [0] * (len(s))
    index = 0
    i = 1
    while i < len(s):
        if s[i] == s[index]:
            shiftT[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = shiftT[index-1]
            else:
                shiftT[i] = 0
                i += 1
    return shiftT
    
def KMP(text,pattern):
    shiftT = shiftTable(pattern)
    i = j = 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = shiftT[j-1]
            else:
                i += 1
    if j == len(pattern):
        return True
    return False

print(KMP("acacabacacabacacac","ccacac")) # return False
print(KMP("acacabacacabacacac","bacacac")) # return True