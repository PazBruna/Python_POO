
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
    def novo_nome(self, novo_nome): #encapsulando o comportamento do nome iniciar com letra mai
        self._nome = novo_nome.title()
    
    @property
    def recomendado(self):
        return self._recomendado

    def recomendar(self):
        self._recomendado += 1
    

class Filme(Programa): #herdando classe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #Chamando o inicializador da classe "mãe" 
        self.duracao = duracao
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
   
vingadores = Filme('Vingadores', 2018, 160)
pantera = Filme('Pantera', 2018, 95)
supernatural = Serie('Supernatural', 2018 , 13)

pantera.dar_like()
supernatural.dar_like()
supernatural.dar_like()
supernatural.recomendar()
vingadores.dar_like()
pantera.recomendar()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes} - Recomendado: {vingadores.recomendado} vezes')
print(f'Nome: {pantera.nome} - Ano: {pantera.ano} - Duração: {pantera.duracao} - Likes: {pantera.likes} Recomendado: {pantera.recomendado} vezes')
print(f'Nome: {supernatural.nome} - Ano: {supernatural.ano} - Duração: {supernatural.temporadas} - Likes: {supernatural.likes} Recomendado: {supernatural.recomendado} vezes')


