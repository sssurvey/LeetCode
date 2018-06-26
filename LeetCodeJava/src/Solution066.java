// 066

public class Solution066 {
    public static void main(String[] args){
        Solution066Solution my_solution = new Solution066Solution();
        int testArray []= new int[3];
        testArray[0] = 1;
        testArray[1] = 2;
        testArray[2] = 3;
        my_solution.plusOne(testArray);
    }

}

class Solution066Solution{
    public int[] plusOne(int[] digits){
       StringBuilder tempString = new StringBuilder();
       for (int digit : digits){
           tempString.append(digit); //transfer list to string
       }
       int operation_int = Integer.parseInt(tempString.toString()); // string -> int
       operation_int++;
       String temp_string = String.valueOf(operation_int);
       int [] answer = new int[temp_string.length()];
       int temp_int_holder;
       for(int i = 0; i < temp_string.length(); i++)
       {
            char c = temp_string.charAt(i);
            temp_int_holder = Character.getNumericValue(c);
            //System.out.println(temp_int_holder);
            answer[i] = temp_int_holder;
            //loop through the char in the string to convert them into int
       }
       return answer;
    }
}
