class Solution:
    """
    先看207
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courese2nextcourses = {}
        flags = {}
        courseindegree = {}
        for i in range(numCourses):
            courese2nextcourses[i] = []
            flags[i] = 0
            courseindegree[i] = 0
        for nextcourse, course in prerequisites:
            courese2nextcourses[course].append(nextcourse)
            courseindegree[nextcourse] += 1
        startcourses = []
        for course in courseindegree:
            if courseindegree[course] == 0:
                startcourses.append(course)
        res = []
        for course in startcourses:
            if self.dfs(course, courese2nextcourses, flags, res) == False:
                return []
        if len(res) != numCourses: #因为有可能单独存在一个环，这个环的所有节点indegree均大于0，所以都不在startcourses里
            return []
        res.reverse()
        return res
    def dfs(self, course, courese2nextcourses, flags, res):
        if flags[course] == 1:
            return False
        elif flags[course] == -1:
            return True
        else:
            flags[course] = 1
            for nextcourse in courese2nextcourses[course]:
                if self.dfs(nextcourse, courese2nextcourses, flags, res) == False:
                    return False
            flags[course] = -1
            res.append(course)
            return True

            