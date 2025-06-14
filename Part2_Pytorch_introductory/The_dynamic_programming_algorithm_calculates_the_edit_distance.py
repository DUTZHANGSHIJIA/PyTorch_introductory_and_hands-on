def min_distance(word1: str, word2: str):
    m, n = len(word1), len(word2)

    # Create a DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from word1
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters to form word2

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,   # Deletion
                               dp[i][j - 1] + 1,   # Insertion
                               dp[i - 1][j - 1] + 1)  # Replacement

    return dp[m][n]

#test
word1 = "hello"
word2 = "git"
print(min_distance(word1, word2))  # Output: 3