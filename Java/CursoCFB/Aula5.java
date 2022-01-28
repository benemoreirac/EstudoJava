import java.util.Scanner;

public class Aula5{
    public static void main(String [] args) {
        Scanner entrada = new Scanner(System.in);


        System.out.println("Laço FOR");
        for(int cont=10; cont>0; cont--){
            System.out.print(cont+ ", ");
        }
        System.out.println("");

        System.out.println("Laço WHILE");
        int max = entrada.nextInt();
        int contWhile = 0;
        while(contWhile<max){
            System.out.print("Nº "+ contWhile + ", ");
            contWhile++;
        }

        System.out.println("Laço DO-WHILE");
        int contDo = 0;
        do{
            System.out.print("Nº "+ contDo + ", ");
            contDo++;
        }while(contDo<=20);
    }
}