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

    def imprime(self):
        print(f'{self._nome} - {self.ano} - Likes: {self._likes} - Recomendado: {self._recomendado} vezes')

class Filme(Programa): #herdando classe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #Chamando o inicializador da classe "mãe" 
        self.duracao = duracao
    
    def imprime(self):
        print(f'{self._nome} - {self.ano} - Duração: {self.duracao}min - Likes: {self._likes} - Recomendado: {self._recomendado} vezes')
  
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - Likes: {self._likes} - Recomendado: {self._recomendado} vezes')

vingadores = Filme('Vingadores', 2018, 160)
pantera = Filme('Pantera', 2018, 95)
supernatural = Serie('Supernatural', 2018 , 13)

pantera.dar_like()
supernatural.dar_like()
supernatural.dar_like()
supernatural.recomendar()
vingadores.dar_like()
pantera.recomendar()

filmes_series = [vingadores, pantera, supernatural]

for programa in filmes_series:
    programa.imprime()

print(isinstance(vingadores, Serie))
