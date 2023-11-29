import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()) {
    val stairCount = readLine().toInt()
    val stairs = mutableListOf<Int>()
    val dp = Array(stairCount + 1) { 0 }
    stairs.add(0)
    repeat(stairCount) {
        stairs.add(readLine().toInt())
    }

    dp[1] = stairs[1]
    if (stairCount == 1) {
        println(stairs[1])
        return
    }
    dp[2] = stairs[1] + stairs[2]
    for (i in 3..stairs.lastIndex) {
        dp[i] = max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2])
    }
    println(dp[stairCount])
}
