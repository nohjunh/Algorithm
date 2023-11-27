lateinit var visited: MutableList<Boolean>
lateinit var answer: MutableList<String>
val temp = mutableListOf<String>()

class Solution {
    fun solution(tickets: Array<Array<String>>): Array<String> {
        visited = MutableList(tickets.size) { false }
        answer = mutableListOf()

        tickets.sortBy { it[1] }
        dfs("ICN", tickets, 0)
        return answer.toTypedArray()
    }
}

fun dfs(start: String, tickets: Array<Array<String>>, depth: Int) {
    temp.add(start)

    if (depth == tickets.size){
        answer.addAll(temp)
        return
    }

    for(i in tickets.indices){
        if (tickets[i][0] == start && !visited[i]){
            visited[i] = true
            if (answer.isNotEmpty()) return
            dfs(tickets[i][1], tickets, depth + 1)
            visited[i] = false
        }
    }
    temp.removeAt(temp.lastIndex)
}
