
public class TestaGetESet {
	public static void main(String[] args) {
		Conta conta = new Conta();
		conta.setNumero(1337);
		System.out.println("Conta usando Get: " + conta.getNumero());
		
		Cliente paulo = new Cliente();
		
		paulo.setNome("Paulo Silveira");
		conta.setTitular(paulo);
		System.out.println("Nome do Titular: "+conta.getTitular().getNome());
		
		conta.getTitular().setProfissao("programador");
		System.out.println("PRofissão: "+ conta.getTitular().getProfissao()); 
		
	}

}


