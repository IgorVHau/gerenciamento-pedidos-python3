class ObservadorStatus:
    def __init__(self, notificacoes):
        self.notificacoes = notificacoes
    
    def atualizar(self, pedido):
        mensagem = f"O pedido foi atualizado para: {pedido.status}"
        self.notificacoes.enviar_notificacoes(pedido.cliente, mensagem)
