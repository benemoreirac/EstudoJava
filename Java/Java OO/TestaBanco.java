
public class TestaBanco {
	public static void main(String[] args) {
		
		Cliente bene = new Cliente();
		bene.nome = "Ebenezer Moreira";
		bene.cpf = "222.222.222-22";
		bene.profissao = "programdaror";
		
		Conta contaDoBene = new Conta();
		contaDoBene.deposita(100);
		
		contaDoBene.titular = bene;
		System.out.println(contaDoBene.titular.nome);
		System.out.println(contaDoBene.titular);
		System.out.println(bene);
		
		
	}

}
