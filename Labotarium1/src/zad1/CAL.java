package zad1;

public class CAL {
    public int SUM(int a, int b) {
        return a + b;
    }

    public int SUB(int a, int b) {
        return a - b;
    }

    public int MUL(int a, int b) {
        return a * b;
    }

    public int DIV(int a, int b) {
        if(b == 0) {
            throw new IllegalArgumentException("You can't divide by 0");
        } else {
            return a / b;
        }
    }
}