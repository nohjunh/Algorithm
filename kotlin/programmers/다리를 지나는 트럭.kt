import java.util.*

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var answer = 0

        val bridgeQueue: Queue<Int> = LinkedList<Int>()
        val waitingQueue: Queue<Int> = LinkedList<Int>()
        truck_weights.forEach { weight ->
            waitingQueue.add(weight)
        }
        repeat(bridge_length) {
            bridgeQueue.add(0)
        }

        while(waitingQueue.isNotEmpty()) {
            answer++
            bridgeQueue.poll()
            if (weight >= waitingQueue.peek() + bridgeQueue.sum()) {
                bridgeQueue.add(waitingQueue.poll())
            } else {
                bridgeQueue.add(0)
            }
        }

        while(bridgeQueue.isNotEmpty()) {
            answer ++
            bridgeQueue.poll()
        }

        return answer
    }
}
