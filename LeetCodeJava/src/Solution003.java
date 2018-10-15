public class Solution003 {

    // need to change for loop to do while loop
    public static String solution(String string) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        char[] charArr = string.toCharArray();
        for (char aCharArr : charArr) {
            if (sb.toString().indexOf(aCharArr) == -1) {
                sb.append(aCharArr);
            } else if (sb.toString().indexOf(aCharArr) >= 0 && sb.toString().length() > answer
                .length()) {
                answer = sb.toString();
                sb = new StringBuilder();
            }
        }
        return answer;
    }
}

