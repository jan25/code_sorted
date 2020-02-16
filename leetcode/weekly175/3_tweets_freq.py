'''
https://leetcode.com/contest/weekly-contest-175/problems/tweet-counts-per-frequency/

This is still unaccepted. No ideas whats wrong :(
'''
from collections import defaultdict

class TweetCounts:

    def __init__(self):
        self.per_min = {}
        self.per_sec = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.per_sec:
            self.per_min[tweetName] = defaultdict(int)
            self.per_sec[tweetName] = defaultdict(int)
        self.per_sec[tweetName][time] += 1
        for i in range(60):
            self.per_min[tweetName][time - i] += 1

    def get_per_min(self, s, e, t):
        pm, ps = self.per_min[t], self.per_sec[t]
        per_min = []
        
        while s + 60 <= e:
            per_min.append(pm[s])
            s += 60
        
        last_min = 0
        while s <= e:
            last_min += ps[s]
            s += 1
        per_min.append(last_min)
        pm, ps = None, None
        return [*per_min]
            
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        print(freq, startTime, endTime)
        pm = self.get_per_min(startTime, endTime, tweetName)
        if freq == 'minute': return [*pm]
        if freq == 'day': return [sum(pm)] # see range of startTime, endTime inputs
        # handle hour freq
        return [sum(pm[i:60]) for i in range(0, len(pm), 60)]


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)