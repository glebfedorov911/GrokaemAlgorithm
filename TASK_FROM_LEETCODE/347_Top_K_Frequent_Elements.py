class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}

        for i in nums:
            if i not in hash_table:
                hash_table[i] = 0
            hash_table[i] += 1

        hash_list = sorted(hash_table.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:k]
        
        return [i[0] for i in hash_list]