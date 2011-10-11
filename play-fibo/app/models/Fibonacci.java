package models;

/**
 * @author huljas
 */
public class Fibonacci {

    public static int fibo(int n) {
        if (n < 2) {
            return 1;
        }
        return fibo(n-1) + fibo(n-2);
    }

    public static long fibo2(int n) {
        long f_2 = 1;
        long f_1 = 1;
        if (n < 2) {
            return 1;
        }
        for (int i = 2; i < n; i++) {
            long f = f_1 + f_2;
            f_2 = f_1;
            f_1 = f;
        }
        return f_1 + f_2;
    }
}
