// https://leetcode.com/contest/weekly-contest-158/problems/dice-roll-simulation/

var mod int64 = 1000000007
var r []int
var memo map[string]int64

func dp(last int, c int, n int) int64 {
    if c > 0 && r[c - 1] < last {
        return 0
    }
    if n == 0 {
        return 1
    }
    s := fmt.Sprintf("%4d%2d%d", n, last, c)
    if v, ok := memo[s]; ok {
        return v
    }
    sol := int64(0)
    for _, nc := range []int{1, 2, 3, 4, 5, 6} {
        nn := 1
        if nc == c {
            nn += last
        }
        sol += dp(nn, nc, n - 1)
    }
    memo[s] = sol % mod
    return memo[s]
}

func dieSimulator(n int, rollMax []int) int {
    memo = map[string]int64{}
    r = rollMax
    return int(dp(0, 0, n))
}
