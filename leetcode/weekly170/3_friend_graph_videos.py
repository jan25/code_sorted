'''
https://leetcode.com/contest/weekly-contest-170/problems/get-watched-videos-by-your-friends/
'''
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        vis = set(friends[id])
        
        q = [*friends[id]]
        ps = len(q)
        while level > 1:
            s = len(q) - ps
            ps = 0
            for i in range(s, len(q)):
                for f in friends[q[i]]:
                    if f not in vis:
                        vis.add(f)
                        q.append(f)
                        ps += 1
            level -= 1
    
        vids = {}
        for i in range(len(q) - ps, len(q)):
            if q[i] == id: continue
            for v in watchedVideos[q[i]]:
                if v not in vids: vids[v] = 0
                vids[v] += 1
        
        p = [(v, k) for k, v in vids.items()]
        p.sort()
        
        return [a[1] for a in p]
