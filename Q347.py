import heapq

def topKFrequent(nums, k):
    dic = {}
    for n in nums:
        dic[n] = dic.get(n, 0) + 1
    
    heap = []
    for key in dic.keys():
        heappush(heap, (dic[key], key))
    
    while len(heap) > k: 
        heappop(heap)
        
    res = []
    while heap:
        res.append(heappop(heap)[1])
    return res
        

    