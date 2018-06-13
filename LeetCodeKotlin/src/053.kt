fun main(args: Array<String>) {
    var my_solution = Solution()
    //val test_array : IntArray = intArrayOf(-2,1,-3,4,-1,2,1,-5,4)
    val test_array : IntArray = intArrayOf(-2,-1,-1)
    println(my_solution.maxSubArray(test_array))
}
/*
    if I already have a number:
        then if I need to use that number to add another number that is negative
        then that means the sum will not become larger, instead, it will only --
        thus for that case, I'd rather give up that num
        Input: [-2,1,-3,4,-1,2,1,-5,4]
        using the sampel input, consider array[0] and [1]
        -2 + 1 = -1 is less than 1, id rather start from 1, drop the [0], and
        continue my problem from [1]

        for nums[i]:
            if nums[i-1] > 0:
                ans.append(nums[i]+nums[i-1])
            else:
               ans.append(nums[i]) //since no need to add negative

        return ans.max()

 */


class Solution {
    fun maxSubArray(nums: IntArray): Int? {
        //return is the sum
        var final_array = IntArray(nums.size) //create an array to hold result
        for (nums_index in final_array.indices){
            if (nums_index == 0) {
                final_array[nums_index] = nums[nums_index]
            }
            else if (nums[nums_index] >= 0 && final_array[nums_index-1] < 0){
                final_array[nums_index] = nums[nums_index]

            } else if (nums[nums_index] <= 0 && nums[nums_index] > final_array[nums_index-1]){
                final_array[nums_index] = nums[nums_index]
            }
            else {
                final_array[nums_index] = final_array[nums_index-1] + nums[nums_index]
            }
        }
        return final_array.max()
    }

}