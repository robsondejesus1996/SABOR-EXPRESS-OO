#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo =  modelo
        self.cor = cor
        self.ano = ano


carro1 = Carro()
carro1.modelo = 'Pulse'
carro1.cor = 'Preto'
carro1.ano = '2024/2024'    

print(vars(carro1))

meu_carro = Carro(modelo='Fusca', cor='Azul', ano=2024)


#Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante():
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

restaurante1 = Restaurante()
restaurante1.nome = "Pizzas restaurante"        
restaurante1.categoria = "Pizzaria"
restaurante1.ativo = True

restaurante_exemplo = Restaurante(nome='Comida Boa', categoria='Gourmet', ativo=True, capacidade=50, nota_avaliacao=4.5)



    

