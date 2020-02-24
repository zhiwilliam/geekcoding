class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if words == [] or s == '':
            return []

        word_length = len(words[0])

        words_dict = collections.defaultdict(int)

        for item in words:
            words_dict[item] += 1

        res = []

        for i in range(0,word_length):

            words_of_window = collections.defaultdict(int)
            num = 0

            start = i

            for j in range(i, len(s), word_length):
                word = s[j:j+word_length]

                if word in words_dict:

                    words_of_window[word] += 1
                    num += 1

                    if words_of_window[word] > words_dict[word]:
                        while s[start:start+word_length] != word:
                            words_of_window[s[start:start + word_length]] -= 1
                            start += word_length
                            num -= 1
                        words_of_window[word] -= 1
                        num -= 1
                        start += word_length
                    if num == len(words):
                        res.append(start)

                else:
                    num = 0
                    words_of_window.clear()
                    start = j + word_length

        return res