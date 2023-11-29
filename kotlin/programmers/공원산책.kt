class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        var curY = 0
        var curX = 0
        val moveY = mapOf('N' to -1, 'S' to 1, 'W' to 0, 'E' to 0)
        val moveX = mapOf('N' to 0, 'S' to 0, 'W' to -1, 'E' to 1)

        for (i in park.indices) {
            for (j in park[i].indices) {
                if (park[i][j] == 'S') {
                    curY = i
                    curX = j
                }
            }
        }

        for (route in routes) {
            val direction = route.split(" ")[0].first()
            var step = route.split(" ")[1].toInt()

            var newY = curY
            var newX = curX

            for (i in 1..step) {
                newY = curY + (moveY[direction] ?: 0) * i
                newX = curX + (moveX[direction] ?: 0) * i

                if (newY < 0 || newX < 0 || newY >= park.size || newX >= park[0].length || park[newY][newX] == 'X') {
                    newY = curY
                    newX = curX
                    break
                }
            }

            curY = newY
            curX = newX
        }

        return intArrayOf(curY, curX)
    }
}