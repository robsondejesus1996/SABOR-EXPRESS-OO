class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhas'    
musica1.artista = 'Quem'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Rima entre amigos'
musica2.artista = 'Cone Crew Diretoria'
musica2.duracao = 420


print(vars(musica1))
print(vars(musica2))
