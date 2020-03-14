from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        queue = deque([(start, 0)])
        while queue:
            cur_str, distance = queue.popleft()
            if cur_str == end:
                return distance
            for i in range(len(cur_str)):
                for c in 'ACGT':
                    new_str = cur_str[:i] + c + cur_str[i+1:]
                    if new_str != cur_str and new_str in bank:
                        queue.append((new_str, distance+1))
                        bank.remove(new_str)
        return -1