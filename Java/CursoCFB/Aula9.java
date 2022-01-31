//Entendendo metodos em Java.
// Sobrecarga de metodos

public class Aula9 {
    public static void main(String [] aegs){
        canal();
        msg("CFB Cursos", 1);
        System.out.println(soma2(10,5 ));
        System.out.println(soma(10,5, 1, 2, 300 ));
        System.out.println(soma(1.5,2.5));

    }

    public static void canal(){
        for (int n=0; n<2; n++){
            System.out.println("Curso");
        }
    }
    public static void msg(String m, int l){
        for(int i=0; i<l; i++){
            System.out.println(m);
        }
    }
    
    public static int soma2(int n1, int n2){
        int res= n1+n2;        
        return res;
    }

    public static int soma(int ... numeros){
        int res=0;
        for (int n:numeros){
            res += n;
        }
        return res;
    }

    public static Double soma(Double ... numeros){
        Double res=0.0;
        for (Double n:numeros){
            res += n;
        }
        return res;
    }


}
