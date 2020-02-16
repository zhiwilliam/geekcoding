class Solution:
    def __init__(self):
        self.nums = None
        self.target = None
        self.result_set = set()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.target = target
        self.exhaustive_find()
        return [list(item) for item in self.result_set]

    def find_the_last_element(self, nums, target):
        for item in nums:
            if item == target:
              return item
            else:
              continue
        return None

    def find_the_other_two_elements(self, nums, target):
        indices = range(len(nums))
        tmp = []
        for i in indices:
            if i+1 > indices[-1]:
                break
            last_element = self.find_the_last_element(nums[:i] + nums[i+1:], target - nums[i])
            if last_element == None:
                continue
            two_ele = sorted([nums[i]] + [last_element])
            if two_ele not in tmp:
                tmp.append(two_ele)
        return tmp

    def find_the_other_three_elements(self, first_element, nums, target):
        indices = range(len(nums))
        tmp = []
        for i in indices:
            if i+1 > indices[-1]:
              break
            rest_elements = self.find_the_other_two_elements(nums[:i] + nums[i+1:], target - nums[i])
            if rest_elements == []:
              continue
            for element in rest_elements:
                three_ele = sorted([first_element] + [nums[i]] + element)
                if three_ele not in tmp:
                    tmp += [three_ele]
        return tmp

    def exhaustive_find(self):
        self.nums = sorted(self.nums)
        # print(self.nums)
        tmp = []
        indices = range(len(self.nums))
        for i in indices:
            if i+1 > indices[-1]:
              break
            rest_elements = self.find_the_other_three_elements(self.nums[i], self.nums[:i] + self.nums[i+1:], self.target - self.nums[i])
            # print(rest_elements)
            if rest_elements == []:
              continue
            tmp += rest_elements
        for result in tmp:
            self.result_set.add(tuple(result))



if __name__ == '__main__':
  S = Solution()
  a = [1,0,-1,0,-2,2]
  t = 0
  b = [-499,-486,-479,-462,-456,-430,-415,-413,-399,-381,-353,-349,-342,-337,-336,-331,-330,-322,-315,-280,-271,-265,-249,-231,-226,-219,-216,-208,-206,-204,-188,-159,-144,-139,-123,-115,-99,-89,-80,-74,-61,-22,-22,-8,-5,4,43,65,82,86,95,101,103,123,149,152,162,165,168,183,204,209,209,220,235,243,243,244,248,253,260,273,281,284,288,290,346,378,382,384,407,411,423,432,433,445,470,476,497]
  c = 3032
  # print(S.fourSum(b, c))

  test = [0,0,0,0]
  S.nums = b
  S.target = c
  print(S.fourSum())
