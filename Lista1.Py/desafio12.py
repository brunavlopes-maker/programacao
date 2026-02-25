salario= float(input("digite o salario atual"))
x = salario*0.15
aumento= salario + x
imposto = aumento * 0.08
salariofinal = aumento - imposto
print("o salario sem aumento era: ",salario)
print("o salario com aumento era: ",aumento)
print("o salario final ficou: ",salariofinal)