import java.util.*

lateinit var graph: Array<Int>
private var ans: ArrayList<Int> = arrayListOf()

private fun bfs(cur: Int, K: Int) {
    val queue: Queue<Int> = LinkedList()
    queue.add(cur)

    while (queue.isNotEmpty()) {
        val q = queue.poll()
        if (q == K) {
            ans.add(graph[q])
        }

        if (q + 1 in 0..100000 && graph[q + 1] == 0) {
            queue.add(q + 1)
            graph[q + 1] = graph[q] + 1
        }
        if (q - 1 in 0..100000 && graph[q - 1] == 0) {
            queue.add(q - 1)
            graph[q - 1] = graph[q] + 1
        }
        if (q * 2 in 0..100000 && graph[q * 2] == 0) {
            queue.add(q * 2)
            graph[q * 2] = graph[q] + 1
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (N, K) = readLine().split(" ").map { it.toInt() }

    graph = Array(100000 + 1) { 0 }
    bfs(N, K)

    println(ans.min())
}
