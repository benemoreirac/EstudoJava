
public class TestaSacaNegativo {
	public static void main(String[] args) {
		
		Conta conta = new Conta();
		conta.deposita(100);
		conta.saca(200);
		
		//FAlse- Meetodo saca da classe conta nao aceita saques maiores que saldo;
		System.out.println(conta.saca(200));
		
		conta.saca(101);
		System.out.println("Saldo: " + conta.pegaSaldo());
	}
	
}
