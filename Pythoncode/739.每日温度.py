# from queue import PriorityQueue
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         pq = PriorityQueue()
#         res = [0 for _ in range(len(T))]
#         prevmin = float("inf")
#         for i in range(len(T)):
#             pq.put((T[i], i))
#             if prevmin >= T[i]:
#                 prevmin = T[i]
#                 continue
#             else:
#                 while not pq.empty():
#                     _, j = pq.get()
#                     if T[j] >= T[i]:
#                         break
#                     else:
#                         res[j] = i - j
#                 pq.put((T[j], j))
#                 prevmin = T[j]
#         return res

class Solution:
    """
    https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while len(stack) > 0 and stack[-1][1] < T[i]:
                j, _ = stack.pop()
                res[j] = i - j
            stack.append((i, T[i]))
        return res