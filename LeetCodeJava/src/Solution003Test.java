import static org.junit.Assert.*;

public class Solution003Test {

    @org.junit.Test
    public void solution1() {
        assertEquals(3, Solution003.solution("abcabcbe"));
    }

    @org.junit.Test
    public void solution2() {
        assertEquals(1, Solution003.solution("bbbbb"));
    }

    @org.junit.Test
    public void solution3() {
        assertEquals(3, Solution003.solution("pwwkew"));
    }

    @org.junit.Test
    public void solution4() {
        assertEquals(2, Solution003.solution("aab"));
    }

    @org.junit.Test
    public void solution5() {
        assertEquals(3, Solution003.solution("abcabcbb"));
    }

    @org.junit.Test
    public void solution6() {
        assertEquals(3, Solution003.solution("dvdf"));
    }

}