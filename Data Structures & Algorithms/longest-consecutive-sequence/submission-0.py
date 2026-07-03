class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class DSU:
            def __init__(self, n):
                self.n = n
                self.rank = [1] * n
                self.parent = [0] * n
                self.size = [0] * n
                for i in range(n):
                    self.parent[i] = i
                    self.size[i] = 1

            def find(self, i):
                if self.parent[i] == i:
                    return i
                else:
                    self.parent[i] = self.find(self.parent[i])
                    return self.parent[i]

            def getSize(self, i):
                return self.size[self.find(i)]

            def merge(self, x, y):
                par_x = self.find(x)
                par_y = self.find(y)
                if par_x != par_y:
                    if self.rank[par_x] == self.rank[par_y]:
                        self.parent[par_y] = par_x
                        self.size[par_x] += self.size[par_y]
                        self.rank[par_x] += 1
                    else:
                        if self.rank[par_x] > self.rank[par_y]:
                            self.parent[par_y] = par_x
                            self.size[par_x] += self.size[par_y]
                        else:
                            self.parent[par_x] = par_y
                            self.size[par_y] += self.size[par_x]

        n = len(nums)
        dsu = DSU(n)
        dp = {}
        for i in range(len(nums)):
            if nums[i] in dp:
                continue
            if nums[i] - 1 in dp:
                dsu.merge(i, dp[nums[i] - 1])
            if nums[i] + 1 in dp:
                dsu.merge(i, dp[nums[i] + 1])
            dp[nums[i]] = i

        mx = 0
        for i in range(len(nums)):
            mx = max(mx, dsu.getSize(i))
        return mx