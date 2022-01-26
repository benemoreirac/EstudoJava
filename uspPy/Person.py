class Person:
  def __init__(self, dados):
    self.nome = dados["firstName"]
    self.sobrenome = dados["lastName"]
    self.idade = dados["idade"]

class Professional(Person):
  def __init__(self, dados):
    super().__init__(dados)
    self.profissao = dados["profissao"]

  def apresentacao(self):
    print("Nome: ", self.nome, self.sobrenome ,", tenho ", self.idade, "anos")
    print(self.profissao)

dados = {
    "firstName":"Ebenézer",
    "lastName":"M. Cavalcante",
    "idade":31,
    "profissao":"Programador Python"
    }

pessoa = Professional(dados)
pessoa.apresentacao()
