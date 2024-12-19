import java.util.*;

public class fat {
    public static void main(String[] args) 
    {
        Scanner scanf = new Scanner(System.in);


        //entrada do numero
        System.out.println("Digite seu numero: ");

        int entrada = scanf.nextInt();

        int total = 1; 

        for(int i = entrada; i > 1; i--) //supondo que entrada >= 2
        {   
            total *= i;
        }

        System.out.println("O valor final do fatorial = " + total);

        scanf.close();
    
    }
}
