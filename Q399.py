class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ufhelper = UnionFind(equations)
        for var, val in zip(equations, values):
            ufhelper.union(var[0], var[1], val)
        res = []
        for var in queries:
            par1 = ufhelper.find(var[0])
            par2 = ufhelper.find(var[1])
            if not par1[0] or not par2[0] or par1[0] != par2[0]:
                res.append(-1.0)
            else:
                res.append(par1[1] / par2[1])
        return res
            

class UnionFind(object):
    def __init__(self, equations):
        self.parents = {}
        for var in equations:
            self.parents[var[0]] = (var[0], 1.0)
            self.parents[var[1]] = (var[1], 1.0)

    def find(self, var):
        if var not in self.parents:
            return (None, None)
        if var == self.parents[var][0]:
            return self.parents[var]
        
        par = self.find(self.parents[var][0]) 
        self.parents[var] = (par[0], self.parents[var][1] * par[1])
        return self.parents[var]

    def union(self, var1, var2, val):
        par1 = self.find(var1)
        par2 = self.find(var2)
        if par1[0] != par2[0]:
            self.parents[par1[0]] = (par2[0], par2[1] * val/par1[1])