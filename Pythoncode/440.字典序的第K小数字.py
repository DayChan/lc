class Solution:
    """
    https://zhuanlan.zhihu.com/p/61661191
    """
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        while True:
            if k == 1: # 第一小的，就是cur
                return cur
            left = cur
            right = cur + 1
            node_num = 0 # 计算以cur为头节点的树的节点数（包括cur节点）
            while left <= n:
                node_num += min(right - left, n + 1 - left)
                right *= 10
                left *= 10
            if k > node_num: #向同一层的后一个节点寻找
                k -= node_num
                cur += 1
            else: #向下一层寻找
                k -= 1
                cur *= 10
        return cur