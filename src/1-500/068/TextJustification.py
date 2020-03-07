from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 储存返回结果
        res = []
        # 记录每次进入小循环时i的值
        flag = 0
        # 每次小循环单词连接而成的字符串
        string = ''
        i = 0
        # 单词之间空格的数目
        space_len = 0
        # 遍历循环所有单词
        while i < len(words):
            # 每次加上一个单词并在单词后加一个空格
            string += words[i] + ' '
            # 当前连接串长度
            length = len(string)
            # 当前连接串长度减一（最后多一个空格）等于目标长度
            if length - 1 == maxWidth:
                # 把当前串去除最后多余的空格并加入res
                res.append(string[:-1])
                # 当前串已加入res可以置为空了
                string = ''
                # flag指向下一个单词的位置
                flag = i + 1
            # 当前连接串长度减一（最后多一个空格）大于目标长度
            elif length - 1 > maxWidth:
                string = ''
                # 需要循环i - flag - 1次，flag上次的位置，又因为最后一个单词要特殊处理
                for j in range(i - flag - 1):
                    # 单词的总长度。length总长度。len(words[i])多加单词的长度。1多加的空格。i个单词有i个空格。flag上次的起始位置
                    word_len = length - len(words[i]) - 1 - i + flag
                    # 第一次直接用目的长度减单词总长度即为可用空格数
                    if j == 0:
                        all_space_len = maxWidth - word_len
                    # 否则每次令总长度减去易用的空格数
                    else:
                        all_space_len -= space_len
                    # 空格总长度除以空格段数能除尽，直接让空格长度为其值
                    if (all_space_len) % (i - 1 - flag - j) == 0:
                        space_len = int((all_space_len) / (i - 1 - flag - j))
                    # 除不尽则取整加一
                    else:
                        space_len = int((all_space_len) / (i - 1 - flag - j)) + 1
                    # 构造单词字符串
                    string += words[flag + j] + ' ' * space_len
                # 除去最后多加的空格
                string = string[:-space_len]
                # 最后一个单词的特殊处理，add_len是最后一个单词之前要填充的空格数
                add_len = maxWidth - len(string) - len(words[i - 1])
                # 最后串如果为空则先写单词再加空格，否则先加空格再写单词
                add_string = words[i - 1] + ' ' * add_len if string == '' else ' ' * add_len + words[i - 1]
                string += add_string
                # 处理好最后一个单词，再加入res
                res.append(string)
                # 标记flag
                flag = i
                # 进来的时候总长度是大于目标长度的，即i多加了1，这里减一
                i -= 1
                # 串置为空
                string = ''
            i += 1
        # 最后如果串不为空，则最后一行没有满，没有进小循环，把串加入str
        if string != '':
            # 除去最后多余的一个空格
            string = string[:-1]
            # 得到尾部需要填充空格的长度
            add_len = maxWidth - len(string)
            # 填充空格
            string += ' ' * add_len
            # 加入res
            res.append(string)
        return res


solution = Solution()
# print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20))
#print(solution.fullJustify(["1", "2"], 16))
