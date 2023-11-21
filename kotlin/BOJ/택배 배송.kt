import java.util.*

data class Node(
    val index: Int,
    val distance: Int
)

lateinit var graph: Array<MutableList<Node>>
lateinit var distance: Array<Int>

fun dijkstra(start: Int) {
    val priorityQueue = PriorityQueue<Node>(compareBy { it.distance })
    priorityQueue.add(Node(start, 0))
    distance[start] = 0

    while (priorityQueue.isNotEmpty()) {
        val (now, dist) = priorityQueue.poll()

        if (distance[now] < dist) continue

        for (next in graph[now]) {
            val cost = dist + next.distance

            if (cost < distance[next.index]) {
                distance[next.index] = cost
                priorityQueue.add(Node(next.index, cost))
            }
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (N, M) = readLine().split(" ").map { it.toInt() }

    graph = Array(N + 1) { mutableListOf() }
    distance = Array(N + 1) { Int.MAX_VALUE }

    repeat(M) {
        val (a, b, c) = readLine().split(" ").map { it.toInt() }
        graph[a].add(Node(b, c))
        graph[b].add(Node(a, c))
    }

    dijkstra(1)
    println(distance[N])
}
