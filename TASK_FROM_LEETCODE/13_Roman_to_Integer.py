class Solution:
    def __init__(self):
        self.symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        self.minus_symbols = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            "XC": 90,
            "CD": 400,
            "CM": 900 
        }

    def romanToInt(self, s: str) -> int:
        sm = 0
        i = 0
        while i < len(s):
            if i+1 < len(s):
                if num := self.minus_symbols.get(s[i:i+2]):
                    sm += num
                    i += 2
                    continue
                else:
                    print(self.symbols.get(s[i]))
                    sm += self.symbols.get(s[i])
            else:
                print(self.symbols.get(s[i]))
                sm += self.symbols.get(s[i])
            i += 1
        return sm