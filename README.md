# Sistema bancário com funções

Desafio "Otimizando o Sistema Bancário com Funções Python" da formação Python
da [DIO](https://www.dio.me/). É a continuação do
[sistema bancário](https://github.com/Ryannzadas/sistema-bancario-python):
cada operação virou uma função e o sistema ganhou usuários e contas correntes.

## Operações

| Opção | Operação      | Regras |
|-------|---------------|--------|
| `d`   | Depositar     | Só valores positivos. |
| `s`   | Sacar         | Até 3 saques por dia, de no máximo R$ 500,00 cada, e só com saldo suficiente. |
| `e`   | Extrato       | Lista todas as movimentações e o saldo atual. |
| `nu`  | Novo usuário  | Nome, data de nascimento, CPF e endereço. O CPF guarda só os números e não pode repetir. |
| `nc`  | Nova conta    | Agência `0001`, número sequencial a partir de 1, ligada a um usuário já cadastrado. Um usuário pode ter várias contas. |
| `lc`  | Listar contas | Mostra agência, número e titular de cada conta. |
| `q`   | Sair          | Encerra o programa. |

## Como as funções recebem os argumentos

| Função | Assinatura | Regra pedida |
|--------|------------|--------------|
| `depositar` | `depositar(saldo, valor, extrato, /)` | só posicionais |
| `sacar` | `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)` | só nomeados |
| `exibir_extrato` | `exibir_extrato(saldo, /, *, extrato)` | `saldo` posicional e `extrato` nomeado |

## Como rodar

Precisa do Python 3.8 ou mais novo. Não há dependências.

```bash
python desafio.py
```
