from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        text_s = {}
        text_t = {}

        for char in s:
            text_s[char] = text_s.get(char,0) + 1
        for char_2 in t:
            text_t[char_2] = text_t.get(char_2,0) + 1
        print(text_s)
        print(text_t)
        if (text_s==text_t):
            return True
        else:
            return False


        