from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = sorted(strs, key=lambda x: len(x))[0]
        j = len(shortest_word)
        while j != 0:
            temp = shortest_word[:j]
            indexes = [i.find(temp) for i in strs]
            if all([indexes[i] == indexes[i+1] for i in range(len(indexes) - 1)]):
                return shortest_word[:j]
            j -= 1  

        return ''