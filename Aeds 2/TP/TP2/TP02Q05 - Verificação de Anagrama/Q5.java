import java.util.*;

public class Q5 {

    public static boolean stop(String input) {
        boolean stop = false;
        int len = input.length();

        if (len == 3 && input.charAt(0) == 'F' && input.charAt(1) == 'I' && input.charAt(2) == 'M') {
            stop = true;
        }

        return stop;
    }

    public static void swap(int a, int b, char[] array)
    {
        char temp = array[a];
        array[a] = array[b];
        array[b] = temp;
    }

    public static boolean sortAndCompare(String str1, String str2, int len) {
        char[] array1 = str1.toCharArray();
        char[] array2 = str2.toCharArray();

        boolean resp = true;
        for (int i = 0; i < len - 1; i++) {
            int last = len - 1 - i;
            int imax1 = 0, imax2 = 0;

            for (int j = 1; j <= last; j++) 
            {
                if (array1[j] > array1[imax1])
                {
                    imax1 = j;
                }
                if (array2[j] > array2[imax2])
                {
                    imax2 = j;
                }
            }

            if (array1[imax1] != array2[imax2]) 
            {
                resp = false;
            } 
            else 
            {
                swap(imax1, last, array1);
                swap(imax2, last, array2);
            }

        }

        return resp;
    }

    public static boolean compare(String str1, String str2) {
        boolean resp = false;

        if (str1.length() == str2.length()) {

            int len = str1.length();

            resp = sortAndCompare(str1, str2, len);
        }

        return resp;
    }


    public static void main(String[] args) {

        Scanner scanf = new Scanner(System.in);

        String input = scanf.nextLine();

        while (!stop(input)) {

            input = input.toLowerCase(); //! tem que fazer isso na mao, mas eu fiquei com preguiça

            String splitted[] = input.split(" - ");
            
            boolean resp = compare(splitted[0], splitted[1]);

            System.out.println(resp ? "SIM" : "NÃO");

            input = scanf.nextLine();
        }

        scanf.close();
    }
}