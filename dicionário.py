loja = {
  "produto1": {"nome": "Caderno", "preco": 2.5, "quantidade": 50},
  "produto2": {"nome": "Caneta", "preco": 1.0, "quantidade": 100},}

def print_loja ():
    print("-----------------------------------------")
    for chave ,valor in loja.items():
        print(chave, valor)

def add_product(cod_prod, nome, preco, quant):
    new_prod = {"nome":nome, "preco":preco, "quantidade":quant}
    loja[cod_prod] = new_prod


print_loja()
add_product("produto3","lapis",2, 100)
print_loja()
