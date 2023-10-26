fun largestNumber(numbers: IntArray): String {
    val strNums = numbers.map { it.toString() }

    if (strNums.all { it == "0" }) {
        return "0"
    }

    val sortedNums = strNums.sortedWith(Comparator { a, b ->
        val order1 = a + b
        val order2 = b + a
        order2.compareTo(order1)
    }
    )
    return sortedNums.joinToString("")
}

class Solution {
    fun solution(numbers: IntArray): String {
        return largestNumber(numbers)
    }
}
