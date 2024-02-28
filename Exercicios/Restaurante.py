
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

print(10*'-----------')
print('Exercicios')

#Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

restaurante_praca.categoria = 'Italiana'
print(vars(restaurante_praca))

#Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante_praca.nome)
nome_do_restaurante = restaurante_praca.nome
print(nome_do_restaurante)


#Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
print(restaurante_pizza.ativo)

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo')   

#Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria. 
categoria = Restaurante.categoria    

#Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistro'
print(vars(restaurante_praca))



#Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza1 = Restaurante()
restaurante_pizza1.nome = 'Pizza Place'
restaurante_pizza1.categoria = 'Fast Food'
print(restaurante_pizza1.nome)

#Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza1.categoria == 'Fast Food':
    print('Sim categoria fast food')
else:
    print('Não categoria não é fast food')    

#Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza1.ativo = True
print(vars(restaurante_pizza1))

#Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_pizza1.nome} - Categoria: {restaurante_pizza1.categoria}')