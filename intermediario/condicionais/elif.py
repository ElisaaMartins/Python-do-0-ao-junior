salario = float(input("Qual seu sálario?"))

if salario <= 3000:
    print ("é junior")
elif salario > 3000 and salario <= 6000:
    print ("é pleno")
elif salario > 6000 and salario <= 15000:
    print ("é senior")
else: 
    print ("é gerente de projetos")
    