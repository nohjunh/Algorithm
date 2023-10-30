import java.util.*

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0
        val q: Queue<Pair<Int, Int>> = LinkedList()
        val pq = PriorityQueue<Int>(Collections.reverseOrder())

        for ((idx, item) in priorities.withIndex()) {
            q.offer(Pair(item, idx))
            pq.offer(item)
        }

        while (q.isNotEmpty()) {
            val cur = q.poll()
            if (cur.first == pq.peek()) {
                pq.poll()
                answer++
                if (cur.second == location) break
            } else {
                q.offer(cur)
            }
        }

        return answer
    }
}
