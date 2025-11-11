import java.util.*;

public class Q3 {
    public static void main(String[] args) {
        
        Scanner scanf = new Scanner(System.in);

        int array[] = new int[10];

        int n = scanf.nextInt(); //! lê o primeiro valor

        for(int i = 0; i < 10; i++)
        {
            array[i] = n;
            //n *= 2;
            n = n * 2;
        }
        
        for(int i = 0; i < 10; i++)
        {
            System.out.print(array[i] + " ");
        }

        scanf.close();
    }
}
