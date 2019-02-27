class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() # Apenas UM _ ele apenas protege
        self.ano = ano
        self._likes = 0
        self._recomendado = 0
        
    @property
    def likes (self):
        return self._likes

    def dar_like (self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def novo_nome(self, novo_nome): #encapsulando o comportamento do nome iniciar com letra maiuscula
        self._nome = novo_nome.title()
    
    @property
    def recomendado(self):
        return self._recomendado

    def recomendar(self):
        self._recomendado += 1

    def __str__(self): #Retorna esse dado como string
        return f'{self._nome} - {self.ano} - Likes: {self._likes} - Recomendado: {self._recomendado} vezes'

class Filme(Programa): #herdando classe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #Chamando o inicializador da classe "mãe" 
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - Duração: {self.duracao}min - Likes: {self._likes} - Recomendado: {self._recomendado} vezes'
  
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - Likes: {self._likes} - Recomendado: {self._recomendado} vezes'

class Playlist(list): #herdando list, após isso a playlist poderá ser utilizada como list em qualquer lugar.
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas) 

vingadores = Filme('Vingadores', 2018, 160)
panico = Filme('Todo mundo em panico', 1999, 100)
pantera = Filme('Pantera', 2018, 95)
supernatural = Serie('Supernatural', 2018 , 13)
demolidor = Serie('Demolidor', 2016, 2)

pantera.dar_like()
supernatural.dar_like()
supernatural.dar_like()
supernatural.recomendar()
supernatural.recomendar() 
supernatural.recomendar()
vingadores.dar_like()
pantera.recomendar()
panico.dar_like()
panico.recomendar()
panico.dar_like()
demolidor.recomendar()
demolidor.dar_like()

playlist = [vingadores, panico, pantera, supernatural, demolidor]
playlist_fds = Playlist('Fim de Semana', playlist)

print(f'Tamanho da playlist: {len(playlist_fds)}')

for programa in playlist_fds: #iterar sobre alguma listagem
  print(programa)

print(isinstance(vingadores, Filme)) #True #verificar se o objeto vingadores pertence a classe serie

print(demolidor in playlist_fds) #verificando se demolidor esta na playlist(boolean)


