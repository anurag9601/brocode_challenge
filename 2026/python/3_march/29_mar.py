class dif_ciph:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_alpha_i = 65
    lower_alpha_i = 97

    result = []

    def __init__(self, string):
        self.string = string

    def __call__(self):
        for char in self.string:
            capital = char.upper()
            char_i = self.alphabet.index(capital)

            if len(self.result) == 0:
                if char == capital:
                    self.result.append(self.upper_alpha_i + char_i)
                else:
                    self.result.append(self.lower_alpha_i + char_i)
            else:
                char_upper_value = self.upper_alpha_i + char_i
                char_lower_value = self.lower_alpha_i + char_i
                self.result.append(abs(char_upper_value - char_lower_value))

        return self.result

print(dif_ciph("Hello")())



