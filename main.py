from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus


cliente = Cliente("Mario", "Alura")
item_um = Item("Pizza", 38.00)
item_dois = Item("Refrigerante", 5.00)
itens = [item_um, item_dois]

taxa_entrega = 7.50
pedido = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido.calcular_total()

tipo_pagamento = input("Escolha o método de pagamento: ").lower()
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

MENSAGEM_PAGO = "O pagamento foi confirmado."
MENSAGEM_PREPARANDO = "O pedido está sendo preparado."
MENSAGEM_ENVIADO = "O pedido saiu para a entrega."

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observadores(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO
