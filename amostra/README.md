# 📈 Sistema de Análise de Notas Escolares

Este é um projeto prático desenvolvido em Python com o objetivo de automatizar o cálculo de médias escolares e determinar o status de aprovação de uma lista de estudantes. 

O projeto cumpre todos os requisitos do desafio de organização de repositórios, versionamento de código e documentação técnica.

## 🔍 O que acontece no código (`script.py`)?

Quando o arquivo `script.py` é executado no terminal, o interpretador do Python realiza as seguintes etapas estruturadas:

1. **Leitura dos Dados:** O programa inicializa um dicionário interno (banco de dados simulado) contendo os nomes dos alunos e uma lista com três notas para cada um deles.
2. **Cálculo da Média Aritmética:** O script percorre a lista de cada aluno, soma todas as suas notas usando a função embutida `sum()` e divide pela quantidade total de notas usando `len()`.
3. **Validação da Situação Cadastral:** Com base no resultado da média obtida, uma estrutura de decisão condicional (`if/elif/else`) avalia o desempenho do estudante e atribui um status automatizado:
   - 🟢 **APROVADO:** Se a média final for **maior ou igual a 7.0**.
   - 🟡 **RECUPERAÇÃO:** Se a média final estiver **entre 5.0 e 6.9**.
   - 🔴 **REPROVADO:** Se a média final for **menor que 5.0**.
4. **Formatação e Saída de Dados:** O sistema limpa as casas decimais das médias, alinha o texto e imprime no terminal um painel de relatório limpo e visualmente organizado com os resultados consolidados de todos os estudantes.

## 🛠️ Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Execução
1. Abra o terminal ou prompt de comando na pasta do projeto.
2. Execute o script com o seguinte comando:
   ```bash
   python script.py
   ```
