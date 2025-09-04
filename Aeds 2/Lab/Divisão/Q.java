import java.util.*;

public class Q {

    public static int compare(int[] array, int a, int b, int mod) {
        int resp = 0;
        if (array[a] % mod > array[b] % mod) {
            resp = 1;
        } else if (array[a] % mod < array[b] % mod) {
            resp = -1;
        }
        if (resp == 0) {
            if (array[a] % 2 == 1 && array[b] % 2 == 0) {
                resp = -1;
            } else if (array[a] % 2 == 0 && array[b] % 2 == 1) {
                resp = 1;
            } else if (array[a] % 2 == 1 && array[b] % 2 == 1) {
                if (array[a] > array[b]) {
                    resp = -1;
                } else if (array[a] < array[b]) {
                    resp = 1;
                }
            } else {
                if (array[a] < array[b]) {
                    resp = -1;
                } else if (array[a] > array[b]) {
                    resp = 1;
                }
            }
        }
        return resp;
    }

    public static void main(String[] args) {

        Scanner scanf = new Scanner(System.in);

        int num = scanf.nextInt();

        int divisor = scanf.nextInt();

        System.out.println(num + " " + divisor);
        while (num != 0 && divisor != 0) {

            int[] array = new int[num];

            for (int i = 0; i < num; i++) {

                array[i] = scanf.nextInt();

            }

            for (int i = 0; i < num - 1; i++) {
                for (int j = 0; j < num - 1 - i; j++) {
                    if (compare(array, j, j + 1, divisor) == 1) {
                        int temp = array[j];
                        array[j] = array[j + 1];
                        array[j + 1] = temp;
                    }
                }
            }

            for (int i = 0; i < num; i++) {
                System.out.println(array[i]);
            }

            num = scanf.nextInt();

            divisor = scanf.nextInt();

            System.out.println(num + " " + divisor);
        }

        scanf.close();
    }
}
