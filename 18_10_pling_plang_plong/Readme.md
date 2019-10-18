# Plig Plong Plang

### 18/10/2019 - Participantes
* Tailor
* Hellen
* Jon
* Karina
* Antonio


### Teorema Quociente-Resto
É uma ideia simples que vem direto da divisão.

Dado qualquer número inteiro A e um número positivo inteiro B, existem inteiros únicos Q e R tal que

```A = B * Q + R onde 0 ≤ R < B```

Quando dividimos A por B, Q é o quociente e R é o resto


Exemplos
```
A = 7, B = 2
7 = 2 * 3 + 1
7 mod 2 = 1
```

```
A = 8, B = 4
8 = 4 * 2 + 0
8 mod 4 = 0
```

```
A = 13, B = 5
13 = 5 * 2 + 3
13 mod 5 = 3
```

https://en.wikipedia.org/wiki/Modulo_operation
https://pt.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-quotient-remainder-theorem

-----

## Problema
Dado um número inteiro positivo, a ideia é encontrar os seguintes sons relacionados a esse número com base no resto:

- quando o resto for 3, adicionar 'Pling' ao resultado.
- quando o resto for 5, adicionar 'Plang' ao resultado.
- quando o resto for 7, adicionar 'Plong' ao resultado.
- quando _não tiver_ nenhum dos restos 3, 5 ou 7, o resultado deve ser o próprio número representado como texto. 


Exemplos:
------
Entrada => Saída
```
1 => "1"
3 => "Pling"
5 => "Plang"
7 => "Plong"
8 => "8"
9 => "Pling"
10 => "Plang"
15 => "PlingPlang"
21 => "PlingPlong"
35 => "PlangPlong"
52 => "52"
105 => "PlingPlangPlong"
3125 => "Plang"
```