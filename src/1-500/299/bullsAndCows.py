import operator

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        counters = {str(key): 0 for key in range(0, 10)}
        for i in range(0, len(secret)):
            if secret[i] == guess [i]:
                bulls += 1
            else:
                if counters[secret[i]] < 0:
                    cows += 1
                if counters[guess[i]] > 0:
                    cows += 1
                counters[secret[i]] += 1
                counters[guess[i]] -= 1
        return f'{bulls}A{cows}B'

    def getHint_1(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return f'{bulls}A{both-bulls}B'