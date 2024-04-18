
ent1 = input().split()

# Verificar se a entrada está no formato esperado
if len(ent1) != 3:
    print("Entrada inválida para o produto 1.")
    exit()

codProduto1 = int(ent1[0])
quantProd1 = int(ent1[1])
precoProduto1 = float(ent1[2])


ent2 = input().split()

# Verificar se a entrada está no formato esperado
if len(ent2) != 3:
    print("Entrada inválida para o produto 2.")
    exit()


codProduto2 = int(ent2[0])
quantProd2 = int(ent2[1])
precoProduto2 = float(ent2[2])


valorAPagar1 = quantProd1 * precoProduto1
valorAPagar2 = quantProd2 * precoProduto2


valorFinal = valorAPagar1 + valorAPagar2


print("VALOR A PAGAR : R$ {:.2f}".format(valorFinal))
