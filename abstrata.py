from abc import ABC #abstract base classes
from numbers import Complex
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    pass

filmes = Playlist()

class Numero(Complex):
    def __getitem__(self,item):# Diferente do Java a minha classe que contém um metodo abstrato ele pode ter uma implementação nesse metodo
        super().__getitem__()

#Validação para saber o que será necessário implementar na classe.
