lateinit var visited: ArrayList<Int>
lateinit var network: Array<ArrayList<Int>>
private var infectedCount: Int = 0

private fun dfs(start: Int) {
    visited.add(start)
    for (computer in network[start]) {
        if (computer !in visited) {
            infectedCount++
            dfs(computer)
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

    dfs(1)
    println(infectedCount)
}
