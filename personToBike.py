'''
就是一个2维数组里的有人和自行车，
要每个人匹配到一辆自行车，人和自行车的距离越短越好，
没有距离相同的情况。就是算出所有的距离然后放到heap里慢慢pop出来，记录下人和车的状态就可以了。
'''
import heapq
def personToBike(records):
    '''
    records: List[List[int]]
    row : person 
    col: bike
    '''
    heap = []
    for i in range(len(records)):
        for j in range(len(records[i])):
            heapq.heappush(heap, (records[i][j], (i, j)))
    res = []
    visited_person = set()
    visited_bike = set()
    while len(visited_person) < len(records):
        person = heapq.heappop(heap)
        if person[1][0] not in visited_person and person[1][1] not in visited_bike: 
            visited_person.add(person[1][0])
            visited_bike.add(person[1][1])
            res.append(person[1])
    return res 
test = [[1,2,3],[4,5,6],[7,8,9]]
print (personToBike(test))   