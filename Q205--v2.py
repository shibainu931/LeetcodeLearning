def patternTransfer(s, t):
    check = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in check and t[i] != check[s[i]]:
            return False
        check[s[i]] = t[i]
    return True 

print (patternTransfer('aca', 'dcb'))