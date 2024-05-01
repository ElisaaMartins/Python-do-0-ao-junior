notas = [ ]

contador = 1

while contador <= 5:
    rm = input("RM:")
    nota = float(input("Nota:"))
    resultado = [rm, nota] #cria uma lista com os rm's e as notas
    notas.append(resultado) #atribuiu a variavel notas o valor de resultado, lista dentro de uma lista

    contador = contador + 1 #alternativa: contador =+ 1 

print ("quantidade de notas", len(notas)) #len é para contar qunatas notas tiveram
