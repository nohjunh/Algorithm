lateinit var visited: ArrayList<Int>
lateinit var graph: Array<ArrayList<Int>>
private var count: Int = 0

private fun dfs(start: Int) {
    visited.add(start)
    for (node in graph[start]) {
        if (node !in visited) {
            dfs(node)
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val (N, M) = readLine().split(" ").map { it.toInt() }

    graph = Array(N + 1) { arrayListOf() }
    visited = arrayListOf()

    repeat(M) {
        val (a, b) = readLine().split(" ").map { it.toInt() }
        graph[a].add(b)
        graph[b].add(a)
    }

    for (i in 1..N) {
        if (i !in visited) {
            dfs(i)
            count++
        }
    }

    println(count)
}
