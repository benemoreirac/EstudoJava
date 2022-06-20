
public class TestaEscopo {
	public static void main(String []args) {
		int idade = 18;
		int quantidade = 20;
		int quantidadePessoas = 3;
		boolean acompanhado;
		
		if (quantidadePessoas>=2) {
			acompanhado = true;
		}else {
			acompanhado = false;
		}
		
		System.out.println("Valor do acompanhado" + acompanhado);
		
		if (idade >= 18 || acompanhado) {
			System.out.println("Seja bem vindo");
		} else {
			System.out.println("Infelizmente voce nao pode entrar");					
		}
		
	}

}
