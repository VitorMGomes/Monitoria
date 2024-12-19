import java.util.*;

public class q2{
  public static void main(String args[])
  {
    //achar o maior e o menor de uma sequencia de 10 entradas
    
    Scanner scanf = new Scanner(System.in);
    //
    
    
    int maior; 
    int menor; 
    System.out.println("Escreva o 1º numero: ");
    int entrada = scanf.nextInt(); //primeira entrada
    maior = entrada;
    menor = entrada;
    
    for(int i = 0; i < (10 - 1); i++) //n - 1 entradas restantes
    {
    
      System.out.println("Escreva o " + (i + 2) + "º numero: ");
      entrada = scanf.nextInt();
      
      if(entrada > maior)
      {
        maior = entrada;
      }

      if(entrada < menor)
      {
        menor = entrada;      
      }

    }
    
    System.out.println("Menor: " + menor);
    System.out.println("Maior: " + maior);
    
  
    
    scanf.close();
  }
}


