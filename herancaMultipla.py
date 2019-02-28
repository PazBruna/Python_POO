class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    
    def registra_hora(self, horas):
        print('Horas registradas...')
    
    def mostrar_tarefas(self):
        print('Fez muita coisa..')
    
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')
    
    def busca_cursos_do_mes(self, mes = None):
        print(f'Mostrando cursos - {mes}' if mes else 'mostrando cursos desse mes')
    
class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete')
    
    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do forúm')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Caelum, Alura):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

#MRO
#good head (hierarquia especifica) - Verifica se há outra classe na hierarquia, no caso do pleno, se não houver o metodo na classe Caelum ele irá imprimir o método de Alura.

ricardo = Senior('Ricardo')
print(ricardo)

