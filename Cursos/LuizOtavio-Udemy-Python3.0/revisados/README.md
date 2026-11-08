# Revisões dos exercícios de Luiz Otávio — Udemy

Estas versões revisitam exercícios registrados por **Rafael Tasinato** durante o curso de **Luiz Otávio (Luiz Miranda), na Udemy**. Os arquivos originais foram preservados para permitir a comparação e mostrar a evolução do aprendizado.

As correções dizem respeito às versões de estudo deste repositório e não constituem uma avaliação do material original do professor.

## Arquivos e comparação

| Exercício original | Versão revisada |
| --- | --- |
| [IterandoStringWhile.py](../IterandoStringWhile.py) | [iterando_strings_while_revisado.py](iterando_strings_while_revisado.py) |
| [LacosdeRepeticao.py](../LacosdeRepeticao.py) | [calculadora_while_revisada.py](calculadora_while_revisada.py) |

As duas revisões mantêm programação estruturada, sem classes e sem funções próprias, para destacar sequência, seleção e repetição. A calculadora também introduz tratamento de exceções.

## 1. Iteração de strings com while

### O que precisava mudar

No trecho ativo do original, `letra` recebe a própria entrada do usuário; por isso, a comparação `letra == input_do_usuario` é sempre verdadeira. A escolha em maiúscula é acrescentada antes de cada caractere, em vez de substituir somente as ocorrências desejadas.

### Como a revisão funciona

- Lê a letra da posição atual com `frase[contador]`.
- Compara essa letra com a escolha do usuário, ignorando maiúsculas e minúsculas.
- Usa `if/else` para acrescentar uma única versão do caractere a cada iteração.
- Exige uma única letra e repete a pergunta em caso de entrada inválida.
- Preserva os demais caracteres e continua utilizando `while`.

Exemplo, escolhendo `r` ou `R`:

```text
O Rato Roeu a Roupa do Rei de Roma
```

Uma letra ausente, como `z`, mantém a frase original. A comparação não remove acentos. Para certos caracteres Unicode, a conversão para maiúscula pode produzir mais de um caractere; isso não altera o exemplo fornecido.

## 2. Calculadora com repetição

### O que precisava mudar

O original pede os operandos e o operador antes de verificar a opção de saída. A validação com `isnumeric()` não aceita negativos e decimais usuais e não impede divisão por zero.

### Como a revisão funciona

- Verifica a saída antes de solicitar números.
- Aceita `s` ou `n` com espaços nas extremidades e em maiúsculas/minúsculas.
- Converte os números com `float` e trata entradas inválidas com `try/except`.
- Aceita negativos e decimais com ponto, como `-2.5`.
- Trata divisão por zero e operadores inválidos sem encerrar o programa.
- Rejeita valores não finitos e informa quando o resultado excede a capacidade numérica.
- Retorna à pergunta inicial após o cálculo ou um erro.

Exemplos para conferir:

| Entradas, após responder `n` | Resultado esperado |
| --- | --- |
| `-2.5`, `4`, `+` | `Resultado: 1.5` |
| `8`, `2`, `/` | `Resultado: 4.0` |
| `8`, `0`, `/` | Mensagem de divisão por zero; permite continuar. |
| Texto no lugar de um número | Mensagem de entrada inválida; permite continuar. |
| `8`, `2`, `%` | Mensagem de operador inválido; permite continuar. |
| Responder `s` na pergunta inicial | Encerra sem pedir números. |

`float` usa representação aproximada; resultados como `0.1 + 0.2` podem exibir pequenas diferenças. Este exemplo é didático.

## Como executar

Requisito: **Python 3**, sem dependências externas. Na raiz do repositório:

```bash
python Cursos/LuizOtavio-Udemy-Python3.0/revisados/iterando_strings_while_revisado.py
python Cursos/LuizOtavio-Udemy-Python3.0/revisados/calculadora_while_revisada.py
```

Execute um comando de cada vez. No Windows, também pode utilizar `py`; em outros sistemas, `python3`.

## Atividades de comparação

1. Execute a iteração original e a revisada com a letra `r` e explique a diferença.
2. Localize por que a condição do original era sempre verdadeira.
3. Compare o comportamento das calculadoras ao pedir a saída, dividir por zero e digitar um número negativo.
4. Explique o papel de `break`, `continue` e `try/except` na revisão.

[Voltar ao README principal](../../../README.md)
