class IntegerToRoman:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100,  90,  50,  40,
            10,   9,   5,   4,
            1
        ]
        self.syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

    def convert(self, num):
        result = ""
        for i in range(len(self.val)):
            while num >= self.val[i]:
                result += self.syms[i]
                num -= self.val[i]
        return result

obj = IntegerToRoman()
num = int(input("Enter an integer: "))
print(f"Roman numeral: {obj.convert(num)}")