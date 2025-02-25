from abc import ABC
from abc import abstractmethod


class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self._status = "Criado!"
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, novo_status):
        self._status = novo_status
        print(f"\nO novo status é: {self._status}")

    @abstractmethod
    def calcular_total(self):
        pass
