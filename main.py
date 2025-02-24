from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX


cliente = Cliente("Mario", "Alura")
item_um = Item("Pizza", 38.00)
item_dois = Item("Refrigerante", 5.00)
itens = [item_um, item_dois]

taxa_entrega = 7.50
pedido_retirada = PedidoRetirada(cliente, itens)
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido_retirada.calcular_total()
pagamento_cartao = PagamentoCartao().processar(valor_pedido)
pagamento_pix = PagamentoPIX().processar(valor_pedido)
