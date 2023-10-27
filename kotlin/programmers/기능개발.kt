class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        val result = mutableListOf<Int>()
        var progressList = progresses.toList()
        var speedList = speeds.toList()

        while (progressList.isNotEmpty()) {
            // 진행률 업데이트
            progressList = progressList.zip(speedList) { progress, speed -> progress + speed }

            // 완료된 작업 확인
            var count = 0
            while (progressList.isNotEmpty() && progressList[0] >= 100) {
                progressList = progressList.drop(1)
                speedList = speedList.drop(1)
                count++
            }

            if (count > 0) {
                result.add(count)
            }
        }

        return result.toIntArray()
    }
}
