import java.util.*;

public class q1{

    public static void main(String args[])
    {
        Scanner scanner = new Scanner(System.in);
        
        //vao ser 10 numeros
        
        int total = 0;
        
        for(int i = 0; i < 10; i++)
        {
          System.out.println("Escreva o " + (i + 1) + "º numero: ");
          int in = scanner.nextInt();
          
          total = total + in;
        }
        
        int media = total / 10;
        
        System.out.println("Media e igual a: " + media);
        
        scanner.close();

    }
}
