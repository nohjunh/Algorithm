data class Meeting(
    val start: Int,
    val end: Int,
)

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val meetings = mutableListOf<Meeting>()
    var count = 1

    repeat(n) {
        val (start, end) = readLine().split(" ").map { it.toInt() }
        meetings.add(Meeting(start, end))
    }
    meetings.sortWith(compareBy<Meeting> { it.end }.thenBy { it.start })

    var end = meetings[0].end
    for (i in 1..<n) {
        if (meetings[i].start >= end) {
            count++
            end = meetings[i].end
        }
    }
    println(count)
}
