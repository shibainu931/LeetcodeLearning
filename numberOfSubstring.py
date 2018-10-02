# number of substrings without using all alphabets 
# eg : Alphabet [a, b, c], String : abbacaaaa
# return the number of substrings that does not contain the all alphabets

def countAllSubstring(alphabet, s):
    '''
    alphabet: List[String]
    s: String
    return: int
    '''
    res = 0 
    i = 0 
    queue = []
    checker = set()
    while i < len(s):
        res += 1
        if s[i] not in checker:
            checker.add(s[i])
        queue.append(s[i])
        first = queue[0] if queue else ''
        while len(checker) == len(alphabet) and queue and queue[0] == first:
            queue.pop(0)
        if len(checker) == len(alphabet) and first:
            checker.remove(first)
        res += len(queue) -1
        i +=1
    return res


print (countAllSubstring(['a', 'b', 'c'], 'aabb'))




        