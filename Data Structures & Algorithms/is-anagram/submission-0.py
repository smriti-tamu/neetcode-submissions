from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        text_s = Counter(s)
        text_t = Counter(t)

        if (text_s==text_t):
            return True
        else:
            return False

        