
public class OpcionalAliquotasComIfs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		double salario = 3300.0;
		double impostoRenda;
		
		if(salario >= 1900.0 || salario <= 2800.0) {
			impostoRenda = salario * 0.075; 
			System.out.println("O Imposto de renda é:" + impostoRenda);
			System.out.println("Pode deduzir R$142,00");
		}else {
			if (salario >= 2800.0 || salario <= 3751.0) {
				impostoRenda = salario * 0.15;
				System.out.println("O Imposto de renda é:" + impostoRenda);
				System.out.println("Pode deduzir R$350,00");
			}else {
				if (salario >= 3751.01 || salario <= 4664.00) {
					impostoRenda = salario * 0.225;
					System.out.println("O Imposto de renda é:" + impostoRenda);
					System.out.println("Pode deduzir R$636,00");
				}
			}
		}

	}

}
