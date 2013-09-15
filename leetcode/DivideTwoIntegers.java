/*
 * Divide two integers without using multiplication, division and mod operator.
 */
public class DivideTwoIntegers {
    public int divide(int dividend, int divisor) {
        boolean negative = false;
        if(dividend < 0 && divisor > 0 || dividend >= 0 && divisor < 0)
            negative = !negative;
        long a = Math.abs((long) dividend);
        long b = Math.abs((long) divisor);
        int result = 0;
        while(a >= b) {
            long c = b;
            for(int i = 0; c <= a; i++, c = c << 1) {
                result += 1 << i;
                a -= c;
            }
        }
        return negative ? -result : result;
    }
}