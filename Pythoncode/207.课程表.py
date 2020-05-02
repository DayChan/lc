class Solution:
    """
    https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courese2nextcourses = {}
        flags = {}
        # courseindegree = {}
        for i in range(numCourses):
            courese2nextcourses[i] = []
            flags[i] = 0
            # courseindegree[i] = 0
        for nextcourse, course in prerequisites:
            courese2nextcourses[course].append(nextcourse)
        #     courseindegree[nextcourse] += 1
        # startcourses = []
        # for course in courseindegree:
        #     if courseindegree[course] == 0:
        #         startcourses.append(course)
        for course in courese2nextcourses.keys():
            if self.dfs(course, courese2nextcourses, flags) == False:
                return False
        return True
    def dfs(self, course, courese2nextcourses, flags):
        if flags[course] == 1:
            return False
        elif flags[course] == -1:
            return True
        else:
            flags[course] = 1
            for nextcourse in courese2nextcourses[course]:
                if self.dfs(nextcourse, courese2nextcourses, flags) == False:
                    return False
            flags[course] = -1
            return True

