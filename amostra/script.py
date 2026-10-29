# -*- coding: utf-8 -*-
"""
Desafio Prático - Sistema de Análise de Notas Escolares
Autor: Aluno (Curso de Desenvolvimento)
Descrição: Script em Python que calcula médias e valida o status dos alunos.
"""

def calcular_media(notas):
    """Calcula a média aritmética simples de uma lista de notas."""
    return sum(notas) / len(notas)

def verificar_status(media):
    """Define a situação final do aluno com base na média obtida."""
    if media >= 7.0:
        return "🟢 APROVADO"
    elif 5.0 <= media < 7.0:
        return "🟡 RECUPERAÇÃO"
    else:
        return "🔴 REPROVADO"

def rodar_sistema():
    # Banco de dados simulado de alunos e suas respectivas notas
    alunos_dados = {
        "Amanda Araújo": [8.5, 7.0, 9.0],
        "Carlos Silva": [6.0, 5.5, 6.8],
        "Bruno Santos": [4.0, 3.5, 5.0],
        "Julia Costa": [9.5, 10.0, 9.8]
    }
    
    print("=" * 55)
    print("       SISTEMA DE ANÁLISE DE NOTAS ESCOLARES       ")
    print("=" * 55)
    print(f"{'Nome do Aluno':<20} | {'Média':<7} | {'Situação Final':<15}")
    print("-" * 55)
    
    # Processa e exibe os dados de cada aluno
    for aluno, notas in alunos_dados.items():
        media_final = calcular_media(notas)
        situacao = verificar_status(media_final)
        
        # Formata a exibição da média com uma casa decimal
        print(f"{aluno:<20} | {media_final:<7.1f} | {situacao:<15}")
        
    print("=" * 55)

# Executa o programa principal
if __name__ == "__main__":
    rodar_sistema()
