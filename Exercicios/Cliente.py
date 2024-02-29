# 5) Crie uma classe chamada `Cliente` e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@unidavi', telefone='94546546546545')    
cliente1 = Cliente(nome='Maria', idade=22, email='maria@unidavi', telefone='151462364456')      
cliente3 = Cliente(nome='Robson', idade=27, email='robson@unidavi', telefone='9999999')           

print(vars(cliente3))



        