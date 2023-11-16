import java.util.*

data class Node(
    val index: Int,
    val distance: Int
)

lateinit var graph: Array<MutableList<Node>>
lateinit var distance: Array<Int>

fun dijkstra(start: Int) {
    val priorityQueue = PriorityQueue<Node>(compareBy { it.distance })
    // 시작 노드로 가기 위한 최단거리는 0
    priorityQueue.add(Node(start, 0))
    distance[start] = 0

    while (priorityQueue.isNotEmpty()) {
        val (now, dist) = priorityQueue.poll()

        // 현재 노드가 이미 처리된 노드라면 최단거리 갱신이 불가능하므로 무시
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
    val N = readLine().toInt()
    val M = readLine().toInt()
    distance = Array(N + 1) { Int.MAX_VALUE }
    graph = Array(N + 1) { mutableListOf() }

    repeat(M) {
        val (a, b, c) = readLine().split(" ").map { it.toInt() }
        graph[a].add(Node(b, c))
    }

    val (start, destination) = readLine().split(" ").map { it.toInt() }
    dijkstra(start)

    println(distance[destination])
}
