class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = self._fill_hash_table(s)
        t_hash = self._fill_hash_table(t)

        if len(s_hash) != len(t_hash):
            return False

        for i in s_hash:
            if i not in t_hash:
                return False
            if t_hash[i] != s_hash[i]:
                return False
        return True

    @staticmethod
    def _fill_hash_table(st: str):
        hash_table = {}
        for s in st:
            if not (s in hash_table):
                hash_table[s] = 0
            hash_table[s] += 1

        return hash_table