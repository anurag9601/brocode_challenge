# 6. Zigzag Conversion
# "PAYPALISHIRING"
# P   A   H   N
# A P L S I I G
# Y   I   R

def convert(s, numRows):
    if numRows == 1:
        return s
    
    res = ""
    for r in range(numRows):
        increment = (numRows - 1) * 2
        for i in range(r, len(s), increment):
            res += s[i]
            if r > 0 and r < numRows - 1 and (i + increment - 2 * r) < len(s):
                res += s[i + increment - 2 * r]
    return res

print(convert("PAYPALISHIRING", 3))