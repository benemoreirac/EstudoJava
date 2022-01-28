public class Aula3 {
    public static void main(String [] args) {
        int nota = 39;
        int media = 60;
        int faltas = 10;
        int maxFaltas = 5;
        String resultado ;
        int pos = 10;

        resultado = (nota >= media ? "Aprovado":"Reprovado");
        System.out.println("Resultado Ternaria: " + resultado);

        if(nota>=media && faltas<=maxFaltas){
            System.out.println("Aprovado");
        } else if(nota > 40 && nota < 60){
            System.out.println("Recuperaçãp");
        }else{
            System.out.println("Reprovado");
        }
        System.out.println("Fim do IF");


        switch(pos){
            case 1:
                System.out.println("Primeiro Lugar");
                break;
            case 2:
                System.out.println("Segundo Lugar");
                break;
            case 3:
                System.out.println("Terceiro Lugar");
                break;
            case 4: case 5: case 6:
                System.out.println("Premio de Participação");
                break;
            default:
                System.out.println("Sem premios, Loser!");
                break;


        }
    }
    
}
