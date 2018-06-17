/*
1.     1 -> One 1 or 11
2.     11 -> two 1 or 22
3.     21 -> one 2 one 1 or 1211
4.     1211
5.     111221

This leetCode problem question is extremely confusing, DISLIKE
I made a solution to read the number for example 13566 = 11131526
but turns out what the question want is to represent int by only using 1 or 2, that is is input = 6 then the program
returns 32 since three 2 is 2+2+2 = 6
 */


fun main(args: Array<String>) {
    val my_solution = Solution038()
    //var temp = "1112312"
    //println(temp[6])
    var answerStr = my_solution.countAndSay(1)
    println(answerStr)

}

class Solution038 {
    fun countAndSay(n: Int): String {
        var charArray = n.toString()
        var sb = StringBuilder()
        var answer = charArray[0]
        var current : Char
        var counter = 0

        for (item in charArray) {
            current = item
            if (current == answer) counter++
            else if (current != answer) {
                sb.append(counter)
                sb.append(answer)
                answer = current
                counter = 0 + 1
            }
        }
        sb.append(counter)
        sb.append(charArray[charArray.length-1])
        return sb.toString()
    }

}