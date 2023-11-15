import java.util.*

lateinit var visited: BooleanArray
lateinit var network: Array<ArrayList<Int>>
private var infectedCount: Int = 0

private fun bfs(start: Int) {
    val queue: Queue<Int> = LinkedList()
    queue.add(start)
    visited[start] = true
    while (queue.isNotEmpty()) {
        val q = queue.poll()
        for (computer in network[q]) {
            if (!visited[computer]) {
                queue.add(computer)
                visited[computer] = true
                infectedCount += 1
            }
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val computers = readLine().toInt()
    val pairs = readLine().toInt()

    network = Array(computers + 1) { arrayListOf() }
    visited = BooleanArray(computers + 1) { false }

    repeat(pairs) {
        val (a, b) = readLine().split(" ").map { it.toInt() }
        network[a].add(b)
        network[b].add(a)
    }

    bfs(1)
    println(infectedCount)
}

/////////////////////////////////////////////

import java.util.*

lateinit var network: Array<ArrayList<Int>>
lateinit var visited: ArrayList<Int>
private var infectedCount: Int = 0

private fun bfs(start: Int) {
    val queue: Queue<Int> = LinkedList()
    queue.add(start)
    visited.add(start)

    while (queue.isNotEmpty()) {
        val q = queue.poll()
        for (computer in network[q]) {
            if (computer !in visited) {
                queue.add(computer)
                visited.add(computer)
                infectedCount++
            }
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val computers = readLine().toInt()
    val pairs = readLine().toInt()

    network = Array(computers + 1) { arrayListOf() }
    visited = arrayListOf()

    repeat(pairs) {
        val (a, b) = readLine().split(" ").map { it.toInt() }
        network[a].add(b)
        network[b].add(a)
    }

    bfs(1)
    println(infectedCount)
}