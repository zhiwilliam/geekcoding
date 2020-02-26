class Solution:
    def __init__(self):
        self.result = []
        self._result = self.result.append

    def restoreIpAddresses(self, s):
        if len(s) <= 3:
            return self.result
        self.generateNum('', s, 1)
        return self.result

    def generateNum(self, candidate, s, numCounter):
        if s == '':
            return
        elif numCounter == 4:
            if self.isValid(s):
                self._result(candidate + s)
            else:
                return
        numCounter += 1
        if self.isValid(s[0]):
            tmp = candidate + s[0] + '.'
            self.generateNum(tmp, s[1:], numCounter)
        if self.isValid(s[:2]):
            tmp = candidate + s[:2] + '.'
            self.generateNum(tmp, s[2:], numCounter)
        if self.isValid(s[:3]):
            tmp = candidate + s[:3] + '.'
            self.generateNum(tmp, s[3:], numCounter)

    def isValid(self, num):
        if num.startswith('0') and len(num) > 1:
            return False
        return True if 0 <= int(num) <= 255 else False

if __name__ == '__main__':
  S = Solution()
  IP_S = "25525511135"
  IP_S = "0000"
  IPs = S.restoreIpAddresses(IP_S)
  print(IPs)