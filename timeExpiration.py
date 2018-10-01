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


import numpy as np
import matplotlib as mat

x = np.arrange(0, 3*np.pi, 0.1)
y = np.sin(x)
arr = ['pyplot']
mat.arr[0].plot(x, y)
