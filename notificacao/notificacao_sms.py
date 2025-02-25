from notificacao.notificacao import Notificacao


class NotificacaoSMS(Notificacao):
    def enviar_notificacao(self, cliente, mensagem):
        print(f"Enviando SMS para o {cliente.nome}: {mensagem}")
        