# Dicionarios aninhados
contatos = {"joaofilipe@gmail.com" : {"nome" : "João Filipe", "Tell" : 99999999},
            "miralamazzaro@gmail.com" : {"nome" : "Mirela Mazzaro", "Tell" : 99999999},
            "tobias@gmail.com" : {"nome" : "Tobias", "Tell" : 99999999},
            "marcella@gmail.com" : {"nome" : "Marcella", "Tell" : 99999999},
            "gusta@gmail.com" : {"nome" : "Gustavo", "Tell" : 99999999}
            }
# print(contatos["miralamazzaro@gmail.com"])

######################################################
# Métodos da classe dict(dict é dicionario)
# {}.clear = limpa todos os valores do dicionario
# print(contatos.clear())

# {}.copy = retorna uma copia do dicionario
# print(contatos.copy())

# {}.fromkeys = cria chaves para você, situação um = cria as chaves com valor none, situação dois = cria um conjunto de chaves e coloca um valor padrao
# dict.fromkeys(["a", "b", "c"], "valor padrao")
# print(dict.fromkeys(["a", "b", "c"], "valor padrao"))

# {}.get = acessa valores dentro do dicionario, da pra usar para descobrir se a chave exite dentro do dicionario ou nao, ou caso queria, pode procurar a chave e retornar um valor vazio({})
# print(contatos.get("gustavo@gmail.com", {}))

# .items() = retorna uma lista de tuplas
# for chave, valor in contatos.items():
#     print(chave, valor)

# {}.keys() = retorna uma lista de chaves do dicionario especificado
# print(contatos.keys())

# {}.pop() = remove a chave e o seu valor do dicionario
# print(contatos.pop("gusta@gmail.com"))
# print(contatos.pop("gustavo@gmail.com", {}))
# print(contatos.pop("gusta@gmail.com", "ja foi retirada"))

# {}.popitem() = remove as chaves na sequencia caso nao tenha passado nenhum valor
# print(contatos.popitem())

# {}.setdefault = adiciona a chave e o valor ao dicionario, caso nao exista, se existir, ele retorna o valor da chave existente
# contatos.setdefault("nome", "Peralta")
# print(contatos)
# contatos.setdefault("idade", 20)
# print(contatos)

# {}.update = atualiza os valores do dicionario, com outro dicionario, caso o valor passado nao exista ele ira adiconar no dicionario
# contatos.update({"joaofilipe@gmail.com": {"nome": "Peralta"}})
# print(contatos)

# {}.values() = retorna uma lista com os valores que estao no dicionario
# print(contatos.values())

# {}.in() = forma de saber se uma chave existe ou nao no dicionario
# verificacao = "joaofilipe@gmail.com" in contatos
# print(verificacao)

# {}.del() = voce passa o objeto que deseja remover

# del contatos["joaofilipe@gmail.com"]["tell"] # voce remove apenas o tell
# del contatos["gusta@gmail.com"] # voce remove todo o valor da chave

