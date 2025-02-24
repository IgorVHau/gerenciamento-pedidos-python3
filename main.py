from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery


cliente = Cliente("Mario", "Alura")
item_um = Item("Pizza", 38.00)
item_dois = Item("Refrigerante", 5.00)
itens = [item_um, item_dois]

taxa_entrega = 7.50
pedido_retirada = PedidoRetirada(cliente, itens)
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)

print(f"Cliente: {cliente.nome}, Endereço: {cliente.endereco}")
print(f"Item: {item_um.nome}, Preço: {item_um.preco:.2f}")
print(f"Item: {item_dois.nome}, Preço: {item_dois.preco:.2f}")
print(f"Preço do Pedido Retirada: {pedido_retirada.calcular_total():.2f}")
print(f"Preço do Pedido Delivery: {pedido_delivery.calcular_total():.2f}")
