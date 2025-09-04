import java.util.*;

class Jogador{

    String Nome;
    int Gols = 0;
    int Assists = 0;
    int jogos;

    float Media;


    public void setMedia() {
        this.Media = (this.Gols + this.Assists) / this.jogos;
    }

    public void addGolds(int gols)
    {

    }
}

public class Q1
{   
    public static void main(String args[])
    {
        
        Scanner scanf = new Scanner(System.in);
        
        int n = scanf.nextInt();//numero de jogadores
        scanf.nextLine();

        Jogador[] jogador = new Jogador[n];

        for(int i = 0; i < n; i++)
        {
            String input = scanf.nextLine();

            String splitted[] = input.split(" ");

            
            jogador[i].Nome = splitted[0];
            jogador[i].jogos = (splitted.length - 1) / 2;
            //Colocar gols e assistencia para eles

            jogador[i].setMedia();

        }//! Temos a lista completamente feita e as medias settadas

        //Ordenar por média e desempatar por nome;

        //Printar a lista toda


        scanf.close();

    }
}   