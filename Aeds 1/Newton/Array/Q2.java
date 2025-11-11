import java.util.*;


class Q2
{
    public static void main(String[] args) {
        
        Scanner scanf = new Scanner(System.in);

        int array[] = new int[10];

        for(int i = 0; i < 10; i++)
        {
            array[i] = scanf.nextInt();
            
        } // para o usuario preencher todos os 10 valores

        int x = 0;

        for(int i = 0; i < 10; i++)
        {
            x += array[i] * i;
        }

        float media = x /10;

        System.out.println("A média é:  " + media);

        scanf.close();

    }
}

