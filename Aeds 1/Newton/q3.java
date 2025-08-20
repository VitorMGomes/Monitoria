import java.util.*;

public class q3{
  public static void main(String args[])
  {
    Scanner scanf = new Scanner(System.in);
    
    System.out.println("Escreva um numero maior que 100: ");
    
    int entrada = scanf.nextInt();
    boolean primo = true;
    
    
    for(int i = 2; i < entrada; i++)
    {
      int divisao = entrada % i;
      
      if(divisao == 0)
      {
        primo = false;
        i = entrada; // break
      }
    }
    
    if(primo == true)
    {
      System.out.println("E primo");
    }
    else
    {
      System.out.println("Nao e primo");
    }

    
  }
}


