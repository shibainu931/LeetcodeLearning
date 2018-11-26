'''
 跟猜数字游戏很像，但是更general一点：让你猜几种颜色的组合，有一个长为n的array，每个位置是一个颜色，比如red，blue等等，然后游戏规则是给定一个已知颜色组合的array，让你猜这些颜色是啥。然后有个API可以调用，叫getGuessResult(Collor[] guess), 返回格式如下:
{
  "Correct": 1,
  "Partial Correct": 2
  "Incorrect": 3
}
意思是既猜对颜色并且猜对位置的有1个，猜对颜色但是位置不对的有两个，完全不在已知颜色组合中的有3个。而且有种特殊情况：比如input = ["Red", "Blue", "Yellow", "Red"], guess=["Red", "Red", "Red", "White"], result应该是
{
  "Correct": 1,
  "Partial Correct": 1
  "Incorrect": 2
}

面试官解释说第一个red是correct， 第二个red是partial，第三个red不应该是partial，因为第二个Red已经对应了input中的第四个red。
'''

def guessColorFunc(inputColor, guessColor):
    '''
    inputColor: List[String]
    guessColor: List[String]
    return: HashMap<String, int>
    '''
    store = {}
    for i in inputColor:
        if i in store:
            store[i] +=1
        else:
            store[i] = 1
    res = {'Correct': 0,
           'Partial Correct': 0,
           'Incorrect': 0 }
    for i in range(len(guessColor)):
        if guessColor[i] in store:
            if guessColor[i] == inputColor[i]:
                res['Correct'] += 1
                store[guessColor[i]] -= 1
        if guessColor[i] not in store or store[guessColor[i]] == 0 :
            res['Incorrect'] += 1
    for i in range(len(guessColor)):
        if guessColor[i] in store and guessColor[i] != inputColor[i]:
            if store[guessColor[i]] > 0:
                res['Partial Correct'] += 1
                store[guessColor[i]] -= 1
            else:
                res['Incorrect'] += 1
    print (res)
    return res 

#guessColorFunc(["Red", "Blue", "Yellow", "Red"], ["Red", "Red", "Red", "White"])
