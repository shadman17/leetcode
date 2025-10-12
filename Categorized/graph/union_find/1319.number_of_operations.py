class Disjointset:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def findParent(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.findParent(n1), self.findParent(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        disjointset = Disjointset(n)
        
        extra_edge = 0
        for n1, n2 in connections:
            result = disjointset.union(n1, n2)
            if not result:
                extra_edge += 1
        
        ds = 0
        for i in range(n):
            if disjointset.par[i] == i:
                ds += 1

        return ds - 1 if ds - 1 <= extra_edge else -1