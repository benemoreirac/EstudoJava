
public class TestaValores {
	public static void main(String[] args) {
		Conta conta = new Conta(1337,24226);
		System.out.println(conta.getAgencia());		
		
		Conta conta1 = new Conta(1337,24221);
		System.out.println(conta.getAgencia());		
		
		Conta conta2 = new Conta(1337,24222);
		System.out.println(conta.getAgencia());		
		
		System.out.println("Total de COntas criadas: "+Conta.getTotal());
	}

}
