import java.util.*;

class Presente {
    String nome = "";
    int preferencia = 0;
    float preco = 0;
}

public class Q1 {

    public static int compare(Presente a, Presente b) {
        int resp = 0;

        if (a.preferencia > b.preferencia) {
            resp = 1;
        } else if (a.preferencia < b.preferencia) {
            resp = -1;
        }

        if (resp == 0) {
            if (a.preco - b.preco < 0) {
                resp = 1;
            } else if (a.preco - b.preco >   0) {
                resp = -1;
            }
        }

        if (resp == 0) {
            resp = a.nome.compareTo(b.nome);
        }

        return resp;
    }

    public static void main(String[] args) {

        Scanner scanf = new Scanner(System.in);

        while (scanf.hasNext()) {
            String input = scanf.nextLine();
            String splitted[] = input.split(" ");

            String nomePessoa = splitted[0]; // nome da pessoa
            int tamLista = Integer.parseInt(splitted[1]); // tamanho da lista

            Presente[] presentes = new Presente[tamLista];

            for (int i = 0; i < tamLista; i++) {
                presentes[i] = new Presente();
                presentes[i].nome = scanf.nextLine();

                String line = scanf.nextLine();
                String splitted2[] = line.split(" ");

                presentes[i].preco = Float.parseFloat(splitted2[0]);
                presentes[i].preferencia = Integer.parseInt(splitted2[1]);
            }

            for (int i = 0; i < tamLista; i++) {
                for (int j = 0; j < tamLista - 1 - i; j++) {
                    if (compare(presentes[j], presentes[j + 1]) > 0) {
                        Presente aux = presentes[j];
                        presentes[j] = presentes[j + 1];
                        presentes[j + 1] = aux;
                    }

                }
            }

            System.out.println("Lista de " + nomePessoa);
            for (int i = tamLista - 1; i >= 0; i--) {
                System.out.println(presentes[i].nome + " - R$" + String.format("%.2f", presentes[i].preco));
            }

            if(scanf.hasNext())
            {
                System.out.println();
                scanf.nextLine();
            }
        }

        scanf.close();
    }
}