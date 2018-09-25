class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times 
        self.check = {}
        self.count = {}
        current_vote = 0
        for i in range(len(persons)):
            if persons[i] in self.check:
                self.check[persons[i]] += 1
            else:
                self.check[persons[i]] = 1
            if self.check[current_vote] <= self.check[persons[i]]:
                    current_vote = persons[i]
            self.count[times[i]] = current_vote
        
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        current = self.binarySearch(t)
        if self.times[current] in self.count:
            return self.count[self.times[current]]
        if current + 1 < len(self.times) and self.times[current+1] - t < t- self.times[current]:
            return   self.count[self.times[current+1]]
        return self.count[self.times[current]]

    def binarySearch(self, n):
        i = 0 
        j = len(self.times) 
        while i + 1 < j :
            mid = (i + j) // 2
            if self.times[mid] < n:
                i = mid
            elif self.times[mid] == n:
                return mid
            else:
                j = mid
        return i 
        