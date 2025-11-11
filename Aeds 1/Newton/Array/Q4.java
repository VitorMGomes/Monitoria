import java.util.*;

public class Q4 {
    public static void main(String[] args) {
        
        Scanner scanf = new Scanner(System.in);

        int m1 = 3;
        int m2 = 2;

        int matriz1[][] = new int[m1][m1];
        int matriz2[][] = new int[m2][m2];

        for(int i = 0; i < m1; i++)
        {
            for(int j = 0; j < m1; j ++)
            {
                matriz1[i][j] = scanf.nextInt();
            }   
        }

        
        for(int i = 0; i < m2; i++)
        {
            for(int j = 0; j < m2; j ++)
            {
                matriz2[i][j] = scanf.nextInt();
            }   
        }


        int mr;
        if(m1 > m2)
        {
            mr = 1;
        }
        else
        {
            mr = m2;
        }

        int matrizRes[][] = new int[mr][mr]

        scanf.close();
    }
}
