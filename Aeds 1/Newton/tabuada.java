import java.util.*;

public class tabuada {
    public static void main(String[] args) {
        
        Scanner scanf = new Scanner(System.in);
        int entrada = scanf.nextInt();

        for(int i = 1; i <= entrada; i++)
        {   
            int tabuadaAtual = i; 

            for(int j = 0; j <= 10; j++)
            {
                System.out.println(tabuadaAtual + " x " + j + " = " + (tabuadaAtual * j));
            }
            System.out.println();
            System.out.println();
            System.out.println();
        }   
        


        scanf.close();
    }
}
