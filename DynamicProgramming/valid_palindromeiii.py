def isValidPalindrome(s, k):
    rev = s[::-1]
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[n][n])
    return n - dp[n][n] <= k

print(isValidPalindrome("ABCCBA", 2))
print(isValidPalindrome("a6edfca", 2))
print(isValidPalindrome("waterrfetawx", 2))
