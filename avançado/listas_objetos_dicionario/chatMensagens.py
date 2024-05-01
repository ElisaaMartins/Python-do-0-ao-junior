import os

mensagens = [] # para guardar as mensagens

nome = input("Nome: ")

while True: #começa um loop infinito pq a condição é true

    # limpar o terminal - por comando
    os.system('cls')

    if len(mensagens) > 0: # verificação se a lista de mensagens é maior que 0
        for m in mensagens: 
            print (m['nome'], "-", m["texto"]) # vai percorrer a lista e printar nome e texto


    print ("___________________") # separação

    # obtendo texto
    texto = input("Mensagem: ") 
    if texto == "fim": # verificação se o texto é fim se for ele quebra o loop
        break

    # adicionando mensagem na lista
    mensagens.append ({ # chama a lista mensagens e coloca os elementos adicionados ao final dela
        # dicionario que tem o nome e o texto
        "nome": nome,
        "texto": texto
    })
    