from abc import ABC
from abc import abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass
