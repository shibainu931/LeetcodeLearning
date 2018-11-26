'''
带时间戳expiration的hashmap以及删除expired的entry有一堆task，
有expirationtime，比如1000ms之后expire。然后实现一个generic的hashmap
，能够addtask，gettask（如果task已经expire，就delete）。这两个都实现了，
最后要求加一个可以自动cleanup没有被get过，但是已经expire的task应该可以用HashMap+DoublyLinkedList，
类似LRU的做法。然后定期​从头遍历DLL，删除过期的entryfromDLL&Map。
如果对于所有task，experation是固定值的话，感觉也可以用circulararray做，
这样cleanup会比较快，空间也比较节省，代码大概这样（get时不更新timestamp的写法）
'''

class hashMapWithExpiration(object):

    def __init__(self, expireTime):
        self.timeStore = {}
        self.expireTime = expireTime
        self.notExpireArray = []*self.expireTime

    def get(self, key):
        if key in self.timeStore and isExpired(self.timeStore[key]):
            del self.timeStore[key]
        return self.timeStore[key].val if key in self.timeStore else -1

    def add(self, key, val):
        index = (getCurrentTime % self.expireTime)
        if self.notExpireArray[index] != null:
            del self.timeStore[self.notExpireArray[index]]
        tempNode = node(key, val)
        self.notExpireArray[index] =tempNode
        self.timeStore[key] = tempNode
    
    def isExpired(self, node):
        return  getCurrentTime() - node.expireTime <= self.expireTime
    
    def cleanUp(self):
        for node in self.notExpireArray:
            if self.isExpired(node):
                del self.timeStore[node.key]

class node(object):

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.pre = None 
        self.next = None
        self.expireTime = getCurrentTime()

def getCurrentTime():
    pass
