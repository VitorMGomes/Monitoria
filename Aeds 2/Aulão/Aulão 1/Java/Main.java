import java.util.*;

class Aluno
{
    private String Nome;
    private Double Altura;
    private Boolean Aprovacao;

    Aluno()
    {
       this(" ", 0.0, 0);

    }

    Aluno(String Nome, Double Altura, int Aprovacao)
    {
        this.Nome = Nome;
        this.Altura = Altura;
        setAprovacao(Aprovacao);
    }

    public Double getAltura() {
        return Altura;
    }

    public Boolean getAprovacao() {
        return Aprovacao;
    }

    public String getNome() {
        return Nome;
    }

    public void setAltura(Double altura) {
        Altura = altura;
    }

    public void setAprovacao(int entrada) {
        this.Aprovacao = (entrada == 1) ? true : false;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }

    void readAluno(Scanner scanf)
    {
        String nome = scanf.nextLine();
        Double altura = scanf.nextDouble();
        scanf.nextLine();
        int aprovado = scanf.nextInt();

        setNome(nome);
        setAltura(altura);
        setAprovacao(aprovado);
    }

    @Override
    public String toString()
    {
        return Nome + "; " + Altura + "; " + Aprovacao + ";";
    }
}


public class Main
{

    public static void main(String[] args)
    {
        Scanner scanf = new Scanner(System.in);


        Aluno aluno = new Aluno();

        aluno.readAluno(scanf);


        System.err.println(aluno.toString());


        scanf.close();
    }
}