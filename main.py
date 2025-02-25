from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_email import NotificacaoEmail
from notificacao.notificacao_sms import NotificacaoSMS


cliente = Cliente("Mario", "Alura")
item_um = Item("Pizza", 38.00)
item_dois = Item("Refrigerante", 5.00)
itens = [item_um, item_dois]

taxa_entrega = 7.50
pedido_retirada = PedidoRetirada(cliente, itens)
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido_retirada.calcular_total()
# pagamento_cartao = PagamentoCartao().processar(valor_pedido)
# pagamento_pix = PagamentoPIX().processar(valor_pedido)
tipo_pagamento = input("Escolha o método de pagamento: ").lower()
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento)
pagamento.processar(valor_pedido)

MENSAGEM = "Seu pedido saiu para a entrega!"
notificacao_email = NotificacaoEmail().enviar_notificacao(cliente, MENSAGEM)
notificacao_sms = NotificacaoSMS().enviar_notificacao(cliente, MENSAGEM)
