
public class TesteContas {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ContaCorrente cc = new ContaCorrente(111, 111);
		cc.deposita(100.0);
		
		ContaPoupanca cp = new ContaPoupanca(222, 222);
		cp.deposita(200.0);
		
		cc.transfere(10.0, cp);
		System.out.println("O saldo da conta corrente é: "+cc.getSaldo());
		System.out.println("O saldo da conta poupança é: " + cp.getSaldo());

	}

}
