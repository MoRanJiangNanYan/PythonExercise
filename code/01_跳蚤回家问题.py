from typing import List

'''2021/03/03'''
"""有一只跳蚤的家在数轴上的位置x处。请你帮助它从位置0出发，到达它的家。
跳蚤跳跃的规则如下：
它可以 往前 跳恰好 a个位置（即往右跳）。
它可以 往后跳恰好 b个位置（即往左跳）。
它不能 连续 往后跳 2 次。
它不能跳到任何forbidden数组中的位置。
跳蚤可以往前跳 超过它的家的位置，但是它 不能跳到负整数的位置。
给你一个整数数组forbidden，其中forbidden[i]是跳蚤不能跳到的位置，同时给你整数a，b和x，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x的可行方案，请你返回 -1 。
"""
"""     [参照解:]
from collections import deque
def minimumJumps(forbidden: List[int], a: int, b: int, x: int) -> int:
    forbidden = set(forbidden)
    Q = deque()
    Q.append((0, 0, False))
    while Q:
        cur, cnt, used = Q.popleft()
        if cur == x:
            # 第一次到x即最小步数，因为队列后序元素cnt都是大于等于当前cnt的
            return cnt
        if cur + a < (a + b + x) and cur + a not in forbidden:
            # 6000是往右探索的最大值，x最大为2000
            forbidden.add(cur + a)
            Q.append((cur + a, cnt + 1, False))
            print(Q)
        if not used and cur - b > 0 and cur - b not in forbidden:
            # forbidden.add(cur-b)
            # 这里不能forbidden，因为后退回cur-b处时，无法覆盖前进到cur-b再后退到cur-2b的情况。
            Q.append((cur - b, cnt + 1, True))
            print(Q)
    return -1
"""


class Solution:
    @staticmethod
    def minimumJumps(forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)  # 集合化,优化最小执行次数
        Q = [(0, 0, False)]
        while Q:
            cur, cnt, used = Q.pop(-1)  # 弹出最后一位
            if cur == x:
                return cnt
            if cur < x + a + b and x + a not in forbidden:
                # 执行+a,并记录结果
                forbidden.add(cur + a)  # 若多次执行到某位置,则第一次到达次数最少,可以标定点,进行排除
                Q.append((cur + a, cnt + 1, False))
            if not used and cur - b > 0 and cur - b not in forbidden:
                # 执行-b,并记录结果
                Q.append((cur - b, cnt + 1, True))
            print(Q)
        return -1


# [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,
# 95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
# 29
# 98
# 80
print(Solution.minimumJumps(
    forbidden=[162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149,
               153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6,
               168, 31, 134, 164, 136,72, 98], a=29, b=98, x=80))
