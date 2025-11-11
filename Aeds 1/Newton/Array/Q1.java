import java.util.*;


class Q1
{
    public static void main(String[] args) {
        
        Scanner scanf = new Scanner(System.in);

        int array[] = new int[10];

        for(int i = 0; i < 10; i++)
        {
            array[i] = scanf.nextInt();
        } // le todos os 10 valores

        //! 12 22 11 90 22 33

        for(int i = 0; i < 10; i++)
        {

            if(array[i] % 2 == 0)
            {
                System.out.print(array[i] + " ");
            }

        }// printar os pares

        for(int i = 0; i < 10; i++)
        {
            if(array[i] % 2 != 0 )
            {
                System.out.print(array[i] + " ");
            }
        }//printar os impares


        scanf.close();

    }
}

