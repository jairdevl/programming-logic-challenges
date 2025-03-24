//  Given a set of numbers, return inverse of each. Eache positive number should be converted to negative and vice versa.

public class Inverse {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, -6, -7, -8, -9, -10};
        int[] inverted = invert(numbers);
        for(int i = 0; i < inverted.length; i++) {
            System.out.println(inverted[i]);
        }

    }
    public static int[] invert(int[] numbers) {
        int[] inverted = new int[numbers.length];
        for(int i = 0; i < numbers.length; i++) {
            inverted[i] = -numbers[i];
        }   
        return inverted;
    }
}