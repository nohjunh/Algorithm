import java.util.*

data class Point(
    val x: Int,
    val y: Int
)

lateinit var graph: Array<MutableList<Int>>
lateinit var ans: MutableList<Int>
val dx = arrayOf(0, 0, 1, -1)
val dy = arrayOf(1, -1, 0, 0)

fun bfs(y: Int, x: Int, M: Int, N: Int) {
    val queue: Queue<Point> = LinkedList()
    queue.add(Point(x, y))
    graph[y][x] = 1

    while (queue.isNotEmpty()) {
        val cur = queue.poll()

        repeat(4) {
            val nx = cur.x + dx[it]
            val ny = cur.y + dy[it]

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) return@repeat

            if (graph[ny][nx] == 0) {
                graph[ny][nx] = 1
                ans[ans.size - 1]++
                queue.add(Point(nx, ny))
            }

        }
    }

}

fun main() = with(System.`in`.bufferedReader()) {
    val (M, N, K) = readLine().split(" ").map { it.toInt() }

    graph = Array(M + 1) { MutableList(N) { 0 } }
    ans = mutableListOf<Int>()

    repeat(K) {
        val (leftX, leftY, rightX, rightY) = readLine().split(" ").map { it.toInt() }

        for (y in leftY..<rightY) { // 세로 범위
            for (x in leftX..<rightX) { // 가로 범위
                graph[y][x] = 1
            }
        }
    }

    for (y in 0..<M) {
        for (x in 0..<N) {
            if (graph[y][x] == 0) {
                ans.add(1)
                bfs(y, x, M, N)
            }
        }
    }

    ans.sort()
    println(ans.size)
    println(ans.joinToString(" "))
}
