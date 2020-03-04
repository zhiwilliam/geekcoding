class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not t or not s:
            return ""
        if len(t) > len(s):
            return ""

        dict_t = Counter(t)
        slow, fast = 0, 0
        required = len(dict_t)
        found = 0
        min_length = float('inf')
        start_idx = 0
        while fast < len(s):
            if s[fast] in dict_t:
                dict_t[s[fast]] -= 1
                if dict_t[s[fast]] == 0:
                    found += 1
            while found == required:
                if fast - slow <= min_length:
                    min_length = fast - slow
                    start_idx = slow
                if s[slow] in dict_t:
                    dict_t[s[slow]] += 1
                    if dict_t[s[slow]] == 1:
                        found -= 1
                slow += 1
            fast += 1

        return '' if min_length == float('inf') else s[start_idx: start_idx + min_length + 1]