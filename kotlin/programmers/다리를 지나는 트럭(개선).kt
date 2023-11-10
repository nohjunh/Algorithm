import java.util.*

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var answer = 0

        val bridgeQueue: Queue<Int> = LinkedList<Int>(List(bridge_length){0})
        val waitingQueue: Queue<Int> = LinkedList<Int>(truck_weights.toList())

        while(bridgeQueue.isNotEmpty()) {
            answer++
            bridgeQueue.poll()
            if (waitingQueue.isNotEmpty()) {
                if (weight >= waitingQueue.peek() + bridgeQueue.sum()) {
                    bridgeQueue.add(waitingQueue.poll())
                } else {
                    bridgeQueue.add(0)
                }
            }
        }

        return answer
    }
}
