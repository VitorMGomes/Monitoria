import java.util.Scanner;

public class QE{
    public static int[] preencher(int n){
        Scanner scn = new Scanner(System.in);
        int vet[] = new int[n];
        for(int i =0; i<n; i++){
            vet[i] = scn.nextInt();
            //System.out.println(i);

        }
        return (vet);
    }
     public static int[] ordena(int[] vet, int n, int m){
         int ordem[] = new int[n];
         int div[] = new int[n];
         int aux;

         for(int i = 0; i < n; i++){ //pega p resto da div
             div[i] = vet[i] % m;
             ordem[i] = vet[i];
         }
         for(int j = 0; j < n-1; j++){
             for(int i = 0; i < n-1-j; i++){ //ordena o resto da div
                 if(div[i] > div[i+1]){
                     aux = div[i];
                     div [i] = div[i+1];
                     div [i+1] = aux;

                     aux = ordem[i];
                     ordem [i] = ordem[i+1];
                     ordem [i+1] = aux;
                 }
             }
         }
int cont = 0;
         int j = 0;
         while(cont < m-1){ //percorre por todos os restos possiveis 



             while(j == cont){ // ate acabar a qnt de resto igual


                 if(div[j] == cont){ // ve se o resto e igual ao cont
                     if(ordem[j]%2 != 0){

                         if(ordem[j] < ordem[j+1]){
                         //ordem decrescente
                             aux = ordem[j];
                             ordem [j] = ordem[j+1];
                             ordem [j+1] = aux;
                         }
                     }
                     if(ordem[j]%2 == 0){
                         if(ordem[j] > ordem[j+1]){
                             //ordem crescente
                             aux = ordem[j];
                             ordem [j] = ordem[j+1];
                             ordem [j+1] = aux;
                         }
                     }
                 }
                 j++;
            }
             cont++;
         }
         return (vet);
     }


    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n, m;
        n = scn.nextInt();
        m = scn.nextInt();

        while(n!= 0 && m!=0){
            int vet[];
            vet = preencher(n);
            int ord[];
            ord = ordena(vet, n, m);
            for(int i = 0; i <n; i++){
            System.out.println(ord[i]);
            }

            n = scn.nextInt();
            m = scn.nextInt();
        }
    }
}