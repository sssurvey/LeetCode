package solutions;

public class Solution709 {
    public static String toLowerCase(String string) {
        char[] charArr = string.toCharArray();
        for (int i = 0; i < charArr.length; i++) {
            charArr[i] = Character.toLowerCase(charArr[i]);
        }
        return new String(charArr);
    }
}
