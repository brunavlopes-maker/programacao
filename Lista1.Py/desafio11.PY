dias_trabalhados = int (input("digite o numero de dias trabalhados sem acidente"))

anos = dias_trabalhados // 365
messes = (dias_trabalhados % 365) // 30
dias = (dias_trabalhados % 365) % 30

print(f"'{dias_trabalhados} Dias equivalem a {anos} anos, {messes} messes e {dias} dias,")