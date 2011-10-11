package controllers;

import models.Fibonacci;
import play.mvc.*;


public class Application extends Controller {

    public static void fibo(int n) {
        long fibo = Fibonacci.fibo(n);
        renderText(String.valueOf(fibo));
    }

    public static void fibo2(int n) {
        long fibo = Fibonacci.fibo2(n);
        renderText(String.valueOf(fibo));
    }

    public static void blank() {
      renderText("");
    }
}