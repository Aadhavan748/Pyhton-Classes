class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        result = ""
        for i in range(len(self.s) - 1, -1, -1):
            result += self.s[i]
        return result


s = input("Enter a string: ")
print(Reverse(s).reverse_string())