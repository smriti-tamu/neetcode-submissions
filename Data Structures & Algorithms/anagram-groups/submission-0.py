class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for st in strs:
            count = [0] * 26
            for ch in st:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            if key in seen:
                seen[key].append(st)
            else:
                seen[key]=[st]
        return list(seen.values())
            