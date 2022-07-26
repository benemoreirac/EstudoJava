
public class ContaCorrente extends Conta {
	
	public ContaCorrente(int agencia, int numero) {
		super(agencia, numero);		
	}
	
	@Override
	public boolean saca(double valor) {
		// TODO Auto-generated method stub
		double valorASacar = valor + 0.20;
		return super.saca(valorASacar);
	}

}
