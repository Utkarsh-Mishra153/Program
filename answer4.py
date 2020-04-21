#Creating function to reducing string
def MaxReducedString(s):
    if not s:
        return "Empty String"
    for i in range(0,len(s)):
        if i < len(s)-1:
            if s[i] == s[i+1]:
                return MaxReducedString(s[:i]+s[i+2:])
    return s

print(MaxReducedString('aaabccddd')) # 'abd'
print(MaxReducedString('aa')) # 'Empty String'
print(MaxReducedString('baab')) # 'Empty String'