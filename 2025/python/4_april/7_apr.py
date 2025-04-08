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

# print(convert("PAYPALISHIRING", 3))

# 2. Add Two Numbers ListNode Problem

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry

        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# 11. Container With Most Water
# Solving using two pointer approach

def maxArea(heights):
    lp, rp , ans = 0, len(heights) - 1, 0

    while lp < rp:
        w = rp - lp
        h = min(heights[lp], heights[rp])
        cur_ans = w * h
        ans = max(ans, cur_ans)
        if heights[lp] > heights[rp]:
            rp -= 1
        else:
            lp += 1

    return ans

# print(maxArea([1,8,6,2,5,4,8,3,7]))