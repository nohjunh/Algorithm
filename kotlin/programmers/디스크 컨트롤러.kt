import java.util.*

class Solution {
    fun solution(jobs: Array<IntArray>): Int {
        val priorityQueue = PriorityQueue<Pair<Int, Int>>(Comparator { a, b -> a.second - b.second })
        var totalTime = 0
        var currentTime = 0
        var finishedJobs = 0
        var startTime = -1

        while (finishedJobs < jobs.size) {
            for (job in jobs) {
                if (startTime < job[0] && job[0] <= currentTime) {
                    priorityQueue.add(Pair(job[0], job[1]))
                }
            }
            if (priorityQueue.isNotEmpty()) {
                val (start, duration) = priorityQueue.poll()
                startTime = currentTime
                currentTime += duration
                totalTime += (currentTime - start)
                finishedJobs += 1
            } else {
                currentTime += 1
            }
        }
        return totalTime / jobs.size
    }
}
