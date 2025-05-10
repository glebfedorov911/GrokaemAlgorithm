

class Solution:


    def __init__(self):
        self.decrement_nums = {
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }

        self.nums = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

    def intToRoman(self, num: int) -> str:
        multiplier = 1
        result = ""
        while num:
            last_num = num % 10 * multiplier
            num //= 10
            multiplier *= 10

            roman_num_decrement = self.convert_num_to_roman(self.decrement_nums, last_num)
            roman_num_default = self.convert_num_to_roman(self.nums, last_num)

            if roman_num_decrement == "" and roman_num_default != "":
                result = roman_num_default + result
            elif roman_num_default == "" and roman_num_decrement != "":
                result = roman_num_decrement + result
            else:
                result = min(roman_num_default, roman_num_decrement, key=len) + result

        return result

    def convert_num_to_roman(self, collection_with_nums: dict, num: int) -> str:
        roman_num = ''
        for keys in list(collection_with_nums.keys())[::-1]:
            while num >= keys:
                num -= keys
                roman_num += collection_with_nums.get(keys)

        return roman_num if num == 0 else ""

s = Solution()
r = s.intToRoman(1994)
print(r)