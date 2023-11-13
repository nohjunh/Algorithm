import java.util.*

class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        val map = HashMap<String, Int>()
        players.forEachIndexed { index, name ->
            map[name] = index
        }

        callings.forEach { name ->
            val callIdx = map[name] ?: 0
            val frontName = players[callIdx - 1]

            val callName = players[callIdx]
            players[callIdx] = frontName
            players[callIdx - 1] = callName

            map[callName] = callIdx - 1
            map[frontName] = callIdx
        }

        return players

    }
}