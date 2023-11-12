import java.time.*
import java.time.format.DateTimeFormatter

class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        var answer: IntArray = intArrayOf()
        var termsMap = HashMap<String, Int>()
        terms.forEach { term ->
            val splitTerm = term.split(" ")
            val t = splitTerm[0]
            val d = splitTerm[1].toInt()
            termsMap[t] = d
        }

        val formatter = DateTimeFormatter.ofPattern("yyyy.MM.dd")
        val todayDate = LocalDate.parse(today, formatter)

        privacies.forEachIndexed { idx, privacy ->
            val splitPrivacy = privacy.split(" ")
            val date = LocalDate.parse(splitPrivacy[0], formatter)
            val term = splitPrivacy[1]

            // 입력된 날짜에 월을 더한 날짜 구하기
            val endDate = date.plusMonths(termsMap[term]?.toLong() ?: 0).minusDays(1)

            // 현재 날짜와 비교하여 날짜가 지났는지 확인
            if (todayDate.isAfter(endDate)) {
                answer += idx + 1
            }
        }

        return answer
    }
}