def double_char(s):
    res = ''
    for i in range(len(s)):
        res += s[i] + s[i]
    return res

a = double_char("hello")
