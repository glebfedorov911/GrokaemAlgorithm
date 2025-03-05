class MyHashMap:

    def __init__(self):
        self.hash_table = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hash_table)):
            if key == self.hash_table[i][0]:
                self.hash_table[i] = [key, value]
                break
        else:
            self.hash_table.append([key, value])

    def get(self, key: int) -> int:
        res = [j for i, j in self.hash_table if i == key]
        if not res:
            return -1
        return res[0]
        

    def remove(self, key: int) -> None:
        self.hash_table = [[i, j] for i, j in self.hash_table if i != key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)