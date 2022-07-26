import java.lang.annotation.Retention;

public class Conta {

	private double saldo;
	private int agencia;
	private int numero;
	private Cliente titular;
	private static int total = 0;
	
	public Conta(int agencia, int numero) {
		Conta.total++;
		//System.out.println("O Total de conts é: "+Conta.total);
		this.agencia =agencia;
		this.numero = numero;
		//this.saldo = 100;
		//System.out.println("Estou criando uma conta "+this.numero);	
	}
	
	public void deposita(double valor) {
		this.saldo += valor;		
	}
	
	public boolean saca(double valor) {
		if(this.saldo>-valor) {
			this.saldo -= valor;
			return true;
		}
		return false;
	}	

	public boolean transfere(double valor, Conta destino) {
		if(this.saca(valor)) {
			destino.deposita(valor);
			return true;
		}
		return false;
	}
	
	public double getSaldo() {
		return saldo;
	}
	
	public int getNumero() {
		return numero;
	}
	
	public void setNumero(int numero) {
		if(numero <=0) {
			System.out.println("Não pode valore menor ou = 0");
			return;
		}
		this.numero = numero;
	}
	
	public int getAgencia() {
		return this.agencia;
	}
	
	public void setAgencia(int agencia) {
		if(agencia <=0) {
			System.out.println("Não pode valore menor ou = 0");
			return;
		}
		this.agencia = agencia;
	}
	
	public Cliente getTitular() {
		return titular;
	}
	
	public void setTitular(Cliente titular) {
		this.titular = titular;
	}
	
	public static int getTotal() {
		return Conta.total;
	}
	
}
