import java.util.Scanner;
public class Aula6{
    public static void main(String [] args){
        final int tam = 5;
        int[] num = {10, 20, 21, 22, 23};

        for (int i=0; i<num.length; i++ ){
            System.out.printf(" %d ", num[i]);
        }

        final int tamGab = 5;
        char [] gabarito = {'a','a','d','b','c'};
        char [] respostas = new char[tamGab];
        int nota=0;
        
        Scanner scan = new Scanner(System.in);

        for(int i=0; i<tamGab; i++){
            System.out.printf("%nDigite a %dª resposta: ", i+1);
            respostas[i] = scan.nextLine().charAt(0);
        }

        for(int i=0; i<tamGab; i++){
            if(respostas[i]==gabarito[i]){
                nota++;
            }
        }

        System.out.printf("%nNota do aluno: %d ", nota);

    }
}