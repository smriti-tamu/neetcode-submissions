class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs=""
        for s in strs:
            new_strs+= str(len(s))+"#"+s
        print(new_strs)
        return new_strs

    def decode(self, s: str) -> List[str]:
        i = 0
        final_decoded = []

        while i < len(s):
            j = i

            while s[i] != "#":
                i += 1

            length = int(s[j:i])

            final_decoded.append(
                s[i + 1 : i + 1 + length]
            )

            i = i + 1 + length

        return final_decoded



