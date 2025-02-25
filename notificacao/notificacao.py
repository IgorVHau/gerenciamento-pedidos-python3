from abc import ABC
from abc import abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar_notificacao(self, cliente, mensagem):
        pass
    