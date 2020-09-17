word1 = "horse"
word2 = "ros"

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 初始化一个 len(word1)+1 * len(word2)+1 的矩阵
        dp = [[i+j for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        print(dp)

        for i in range(1, len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        print(dp)
        
        return dp[len(word1)][len(word2)]


s = Solution()
print(s.minDistance(word1,word2))

