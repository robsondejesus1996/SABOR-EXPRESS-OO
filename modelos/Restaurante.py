
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_praca.ativo = False

restaurante_pizza = Restaurante()


restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))