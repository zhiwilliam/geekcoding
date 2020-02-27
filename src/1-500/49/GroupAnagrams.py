from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            res = []
            my_dict = {}
            for i in range(len(strs)):
                # 字符排序并链接为单词
                word = "".join(sorted(strs[i]))
                # 排序后不在字典中，加入并记录排序前的单词做val
                if word not in my_dict:
                    my_dict.update({word: [strs[i]]})
                # 排序后在字典中，加入排序前的单词做val
                else:
                    my_dict[word].append(strs[i])
            # 将字典的val取出做为列表
            for j in my_dict.values():
                res.append(j)
            return res


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
