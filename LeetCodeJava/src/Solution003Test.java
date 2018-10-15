import static org.junit.Assert.*;

public class Solution003Test {

    @org.junit.Test
    public void solution() {
        assertEquals("abc", Solution003.solution("abcabcbe"));
        assertEquals("b", Solution003.solution("bbbbb"));
        assertEquals("kew", Solution003.solution("pwwkew"));
    }
}