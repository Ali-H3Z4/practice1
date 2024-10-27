class CustomStr:
    def __init__(self, str):
        self.str = str

    def custom_split(self, list):
        temp = ""
        final = []
        checker = False
        for i in self.str:
            for j in list:
                if i == j:
                    final.append(temp)
                    temp = ''
                    checker = True
                if checker:
                    break
            if checker:
                checker = False
                continue
            else:
                temp += i
        if temp != '':
            final.append(temp)
        return final


    def remove_duplicate(self):
        result = []
        seen = set()
        for i in self.str:
            if i not in seen:
                seen.add(i)
                result.append(i)
        return "".join(result)

    def set(self, index, new):
        return self.str[:index] + new + self.str[index + 1:]

    def isfloat(self):
        try:
            float(self.str)
            return True

        except ValueError:
            return False

    def ispalindrome(self):
        if self.str[0] == self.str[-1]:
            return True

        else:
            return False
    

a = CustomStr("kdanea")
print(a.ispalindrome())
print(a.isfloat())
print(a.set(2, "u"))
print(a.remove_duplicate())
print(a.custom_split(input("Enter a character: ").split(',')))
print('hi')