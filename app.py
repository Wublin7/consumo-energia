print("=== CALCULADORA DE CONSUMO DE ENERGIA ===")

aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência do aparelho em watts (W): "))
horas = float(input("Quantas horas por dia ele é usado? "))

consumo = (potencia * horas * 30) / 1000

# Valor fixo da energia
valor_kwh = 0.75

# Calcula o custo mensal
custo = consumo * valor_kwh

print("\n=== RESULTADO ===")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f} por mês")
