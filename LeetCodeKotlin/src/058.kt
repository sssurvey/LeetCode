fun main(args: Array<String>) {
    var my_solution = Solution058()
    val test_string = "a aaa    ddddd   df  dfasdf   f"
    var ans = my_solution.lengthOfLastWord4(test_string)
    println(ans)
}


class Solution058 {
    fun lengthOfLastWord(s: String): Int {
        val list = s.split(" ")
        var lastLength = list[0].length
        for (itemindex in list.indices){
            if (list[itemindex].isEmpty()) continue
            else if (list[itemindex].isNotEmpty()) lastLength = list[itemindex].length
        }
        return lastLength
    }

    fun lengthOfLastWord2(s:String):Int{
        val list = s.split(" ")
        val lastLength = list[0].length
        if (list[list.size - 1].isNotEmpty()) return list[list.size - 1].length
        else {
            for (i in 1..list.size){
                if (list[list.size - i].isNotEmpty()) return list[list.size - i].length
            }
        }
        return lastLength
    }

    fun lengthOfLastWord3(s:String):Int{
        val list = s.split(" ")
        val lastLength = list[0].length
        var for_loop = list.size - 1
        while (for_loop > 0){
            if (list[for_loop].isNotEmpty()) return list[for_loop].length
            else for_loop --
        }
        return lastLength
    }

    fun lengthOfLastWord4(s:String):Int{
        var count = 0
        val strlen = s.length - 1
        var beginCount = false
        for (i in strlen.downTo(0)) {
            var char = s[i]
            if (char == ' ') {
                if (beginCount){
                    return count
                }
            } else {
                beginCount = true
                count++
            }

        }
        return count
        }
    }

