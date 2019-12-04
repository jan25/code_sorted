'''
https://leetcode.com/contest/weekly-contest-165/problems/find-winner-on-a-tic-tac-toe-game/
Bruteforce algorithm
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        g = [['-'] * 5 for _ in range(5)]
        for i, m in enumerate(moves):
            c = 'X' if i % 2 == 0 else 'O'
            g[m[0] + 1][m[1] + 1] = c
        a = 0
        for x in range(1, 4):
            for y in range(1, 4):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i != 0 or j != 0:
                            s = set([g[x][y], g[x - i][y - j], g[x + i][y + j]])
                            if len(s) == 1 and g[x][y] != '-':
                                return 'A' if g[x][y] == 'X' else 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'
    