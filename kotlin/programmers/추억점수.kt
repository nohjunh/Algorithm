class Solution {
    fun solution(name: Array<String>, yearning: IntArray, photos: Array<Array<String>>): IntArray {
        val map = name.zip(yearning.toTypedArray()).toMap()
        return photos.map { photo ->
            photo.sumOf { map[it] ?: 0 }
        }.toIntArray()
    }
}