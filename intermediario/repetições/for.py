notas = []

# a função range cria uma lista x = [ 0, 1, 2, 3, 4] -> 5 itens
# range(stop) -> padrão
# range([start], stop, [step])

for x in range(5):
    rm = input("RM:") 
    nota = float(input("Nota:")) #
    resultado = [rm, nota] #cria uma lista com os rm's (posição 0) e as notas (posição 1)
    notas.append(resultado) #atribuiu a variavel notas o valor de resultado, lista dentro de uma lista

print ("quantidade de notas", len(notas)) #len é para contar qunatas notas tiveram

#faz uma lista de notas e o rm's
for n in notas:
    rm = n[0] #pega o rm
    nota = n[1] #pega a nota
    print("O RM", rm, "tirou a nota:", nota)