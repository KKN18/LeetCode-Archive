class Solution:
    def numTilings(self, n: int) -> int:
        f_len = max(4, n+1)
        f = [0 for i in range(f_len)]
        g_len = max(4, n+1)
        g = [0 for i in range(g_len)]

        f[1] = 1
        f[2] = 2
        f[3] = 5

        g[2] = 1
        g[3] = 2

        for i in range(4, n+1):
            f[i] = (f[i-1] + f[i-2] + 2 * g[i-1]) % (10**9 + 7)
            g[i] = (f[i-2] + g[i-1]) % (10**9 + 7)

        return f[n]