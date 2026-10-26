class Solution {
    /**
     * @param {string} text1
     * @param {string} text2
     * @return {number}
     */
    longestCommonSubsequence(text1: string, text2: string): number {
        const l1 = text1.length
        const l2 = text2.length


        const dp = []
        for (let i = 0; i<l1+1; i++){
            dp[i] = Array(l2+1).fill(0)
        }

        for (let rowIndex = l1-1; rowIndex>=0; rowIndex--){
            for (let colIndex = l2-1; colIndex>=0; colIndex--){
                if (text1[rowIndex] == text2[colIndex]){
                    dp[rowIndex][colIndex] = 1 + dp[rowIndex+1][colIndex+1]
                }
                else{
                    dp[rowIndex][colIndex] = Math.max(dp[rowIndex+1][colIndex], dp[rowIndex][colIndex+1])
                }
            }
        }

        return dp[0][0]
    }
}