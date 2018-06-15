/*
1.     1 -> One 1 or 11
2.     11 -> two 1 or 22
3.     21 -> one 2 one 1 or 1211
4.     1211
5.     111221
 */


fun main(args: Array<String>) {
    val my_solution = Solution038()
    var answerStr = my_solution.countAndSay(111231)
    println(answerStr)
}

class Solution038 {
    fun countAndSay(n: Int): String {
        val numberStr : String = n.toString()
        val numberStrList = numberStr.split("")
        val sb = StringBuilder()
        // val integerArray = intArrayOf(0,1,2,3,4,5,6,7,8,9)
        // val strAarry = arrayOf("1","2","3","4","5","6","7","8","9","0")

        var counter = 0
        for (numberStrIndex in numberStrList.indices-1){
            counter++
            if (numberStrList[numberStrIndex] == numberStrList[numberStrIndex+1]){
                counter++
            } else {
                sb.append(counter * numberStrList[numberStrIndex].toInt())
                counter = 0
            }
        }

        return sb.toString()
    }

}