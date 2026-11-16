def obter_valor_numerico(mensagem):
    """Solicita um número ao usuário e garante que a entrada seja válida."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < 0:
                print("⚠️ Por favor, digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Digite apenas números (ex: 1500.50).")


def analisar_orcamento(renda, despesas):
    """Calcula o saldo e retorna o status financeiro."""
    saldo = renda - despesas
    if saldo > 0:
        status = "Superávit (Sobrou dinheiro! 🎉)"
    elif saldo == 0:
        status = "Equilibrado (Contas zeradas ⚖️)"
    else:
        status = "Déficit (Gastos maiores que a renda ⚠️)"
    return saldo, status


def main():
    print("=== 💰 Simulador de Orçamento Mensal ===")
    nome = input("Digite seu nome: ").strip() or "Usuário"

    renda = obter_valor_numerico("Informe sua renda mensal (R$): ")
    despesas = obter_valor_numerico("Informe o total de despesas (R$): ")

    saldo, status = analisar_orcamento(renda, despesas)

    print("\n--- 📊 Resumo Financeiro ---")
    print(f"Titular: {nome}")
    print(f"Renda Mensal: R$ {renda:.2f}")
    print(f"Total de Despesas: R$ {despesas:.2f}")
    print(f"Saldo Final: R$ {saldo:.2f}")
    print(f"Situação: {status}")


if __name__ == "__main__":
    main()

