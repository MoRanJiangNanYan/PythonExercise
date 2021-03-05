"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


def lengthOfLongestSubstring(s: str):
    strset = set(s)  # 获得所有不重复字母
    for i in s:
        if s.count(i) == 1:
            strset.remove(i)
    strlist = s
    for i in strset:
        strlist = '-'.join(strlist.split(i))
    l = strlist.split('-')
    l.sort(key=lambda x: len(x))
    return len(l[-1])+1


print(lengthOfLongestSubstring(s="pwwkew"), '666')
