class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        return commands.map {
            array.slice(it[0]-1..it[1]-1).sorted()[it[2]-1]
        }.toIntArray()
    }
}
