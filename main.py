from cliente import Cliente
from item import Item

cliente = Cliente("Mario", "Alura")
item_um = Item("Pizza", 30.00)
item_dois = Item("Refrigerante", 5.00)

print(f"Cliente: {cliente.nome}, Endereço: {cliente.endereco}")
print(f"Item: {item_um.nome}, Preço: {item_um.preco}")
print(f"Item: {item_dois.nome}, Preço: {item_dois.preco}")
